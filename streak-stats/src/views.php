<?php

declare(strict_types=1);

function renderViewsBadge(): void
{
    // Always set SVG Content-Type first to ensure GitHub proxy receives SVG even on error
    header("Content-Type: image/svg+xml; charset=utf-8");
    header("Cache-Control: no-cache, no-store, must-revalidate");
    header("Pragma: no-cache");
    header("Expires: 0");

    $baseline = 1500;
    $count = 0;

    try {
        $opts = [
            "http" => [
                "method" => "GET",
                "timeout" => 3,
                "header" => "User-Agent: CodeCenturian-ViewCounter\r\n"
            ],
            "ssl" => [
                "verify_peer" => false,
                "verify_peer_name" => false
            ]
        ];
        $context = stream_context_create($opts);
        $response = @file_get_contents("https://api.counterapi.dev/v1/CodeCenturian/profile-views/up", false, $context);

        if ($response !== false) {
            $data = json_decode($response, true);
            if (isset($data["count"])) {
                $count = (int)$data["count"];
            }
        }
    } catch (\Throwable $t) {
        // Fallback gracefully to baseline if network issue
    }

    $totalViews = number_format($baseline + $count);

    echo <<<SVG
<svg xmlns="http://www.w3.org/2000/svg" width="165" height="20" role="img" aria-label="Profile Views: {$totalViews}">
  <title>Profile Views: {$totalViews}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="165" height="20" rx="3" fill="#fff"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="95" height="20" fill="#555"/>
    <rect x="95" width="70" height="20" fill="#00D9FF"/>
    <rect width="165" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <text x="485" y="140" transform="scale(.1)" fill="#fff" textLength="750">Profile Views</text>
    <text x="1300" y="140" transform="scale(.1)" fill="#000" font-weight="bold" textLength="500">{$totalViews}</text>
  </g>
</svg>
SVG;
    exit();
}
