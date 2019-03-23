
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1,width=device-width">
  <meta name="selected-link" value="repo_source">

  
<meta name="octolytics-dimension-device" content="mobile" />
<meta name="octolytics-dimension-user_id" content="25323231" /><meta name="octolytics-dimension-user_login" content="WattanaGaming" /><meta name="octolytics-dimension-repository_id" content="131727758" /><meta name="octolytics-dimension-repository_nwo" content="WattanaGaming/Spammer-Grab-1" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="true" /><meta name="octolytics-dimension-repository_parent_id" content="131018684" /><meta name="octolytics-dimension-repository_parent_nwo" content="Noxturnix/Spammer-Grab" /><meta name="octolytics-dimension-repository_network_root_id" content="115074551" /><meta name="octolytics-dimension-repository_network_root_nwo" content="OraqleFarm/Spammer-Grab" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="9387:EC02:C457DA:12C13BE:5C965FFD" /><meta name="octolytics-dimension-region_edge" content="ams" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">

  <meta class="js-ga-set" name="dimension3" content="mobile">


  

  <title>Spammer-Grab-1/spammer.py at master · WattanaGaming/Spammer-Grab-1 · GitHub</title>

  <link crossorigin="anonymous" media="all" integrity="sha512-o1F0QLAOWTnG6XAL9zMoEWAudbV3JCSFfdlqJF52QyivombevOT/HSloymeqfUiOg21bAch7WTH/DrpX6d1UpA==" rel="stylesheet" href="https://github.githubassets.com/assets/mobile-f0c2db85fd5ea5c04bd9c213e9bba082.css" />


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">




  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="page-responsive">
    


  <header class="Header-old f4 lh-default clearfix">
    <div class="p-responsive flex-justify-between">
        <div class="d-flex flex-justify-between flex-items-center position-absolute right-0 left-0 px-3">
          <a class="brand-logo-invertocat touchable" href="https://github.com/" data-ga-click="Mobile, tap, location:header; text:Logged in logo">
            <svg height="32" class="octicon octicon-mark-github text-white v-align-top" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          </a>

          <div class="px-3 overflow-hidden">
                <div class="css-truncate css-truncate-target width-fit">
    <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
    <strong>
      <a class="text-white" href="/WattanaGaming">WattanaGaming</a>
    </strong> /
    <strong>
      <a class="text-white" href="/WattanaGaming/Spammer-Grab-1">Spammer-Grab-1</a>
    </strong>
  </div>

          </div>

          <div class="d-flex flex-items-center">
            
            <div class="px-3"><!-- placeholder for hamburger --></div>
          </div>
        </div>


        <details class="details-reset">
          <summary class="mt-1 float-right position-relative user-select-none" data-ga-click="Mobile, tap, location:header; text:Hamburger">
            <svg height="24" class="octicon octicon-three-bars notification-indicator" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </summary>
              <div style="clear: both;">
        <div class="py-3">
          <div class="header-search mr-3 scoped-search site-scoped-search js-site-search position-relative "
  role="search"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="131727758" data-scoped-search-url="/WattanaGaming/Spammer-Grab-1/search" data-unscoped-search-url="/search" action="/WattanaGaming/Spammer-Grab-1/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0  js-chromeless-input-container">
            <a class="header-search-scope no-underline" href="/WattanaGaming/Spammer-Grab-1/blob/master/spammer.py">This repository</a>
        <input type="text"
          class="form-control input-sm header-search-input  js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-label="Search this repository"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
      </label>
</form>  </div>
</div>

        </div>
      <ul class="text-bold list-style-none p-0 m-0">
              <li>
                <a class="js-selected-navigation-item HeaderNavlink py-2" data-ga-click="Mobile, tap, location:header; text:Marketplace" href="/marketplace">
                  Marketplace
</a>              </li>
          <li>
            <a href="/explore" data-ga-click="Mobile, tap, location:header; text:Explore" class="js-selected-navigation-item HeaderNavlink py-2">
              Explore
            </a>
          </li>
        <li>
          <a class="js-selected-navigation-item HeaderNavlink py-2" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;mobile header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:&quot;498502910.1551374302&quot;,&quot;originating_request_id&quot;:&quot;9387:EC02:C457DA:12C13BE:5C965FFD&quot;,&quot;originating_url&quot;:&quot;https://github.com/WattanaGaming/Spammer-Grab-1/blob/master/spammer.py&quot;,&quot;referrer&quot;:&quot;https://github.com/WattanaGaming/Spammer-Grab-1/find/master?q=&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="27ebc16bd0dba04c24e929f55a82d664a295d477d3425006a340711ff794df3b" data-ga-click="Mobile, tap, location:header; text:Sign in" href="/login?return_to=%2FWattanaGaming%2FSpammer-Grab-1%2Fblob%2Fmaster%2Fspammer.py">Sign in</a>
        </li>
      </ul>
    </div>

        </details>
    </div>
  </header>



    




<div class="reponav-wrapper lh-default">
  <nav class="reponav js-reponav"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /WattanaGaming/Spammer-Grab-1" href="/WattanaGaming/Spammer-Grab-1">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>


    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /WattanaGaming/Spammer-Grab-1/pulls" href="/WattanaGaming/Spammer-Grab-1/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /WattanaGaming/Spammer-Grab-1/projects" href="/WattanaGaming/Spammer-Grab-1/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>


      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /WattanaGaming/Spammer-Grab-1/pulse" href="/WattanaGaming/Spammer-Grab-1/pulse">
        Pulse
</a>

  </nav>
</div>

<div id="js-flash-container">

</div>




<div class="breadcrumb blob-breadcrumb">
  <label for="blob-history-checkbox" class="blob-history-label">
    <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"/></svg>
  </label>
  <span class="filetype-icon"><svg aria-label="file" class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"/></svg></span>
  <strong class="final-path">spammer.py</strong>
</div>


<input id="blob-history-checkbox"
       class="js-blob-history-checkbox blob-history-checkbox"
       type="checkbox"
       data-url="/WattanaGaming/Spammer-Grab-1/latest_commit/master/spammer.py">

<div class="blob-history">
  <a class="js-blob-history-link" href="/WattanaGaming/Spammer-Grab-1/commits/master/spammer.py">
    Loading latest commit…
</a></div>

<div class="bg-white">
    <div class="blob-file-content js-file-line-container">
      <div class="highlighted-blob tab-size" data-tab-size="8"><div class="code-body highlight"><pre><div class='line js-file-line' id='LC1'><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/python</span></div><div class='line js-file-line' id='LC2'><br></div><div class='line js-file-line' id='LC3'><span class="pl-c"><span class="pl-c">#</span> - Spammer v3.1</span></div><div class='line js-file-line' id='LC4'><span class="pl-c"><span class="pl-c">#</span> | Description: spams a phone number by sending it a lot of sms by using Grab API</span></div><div class='line js-file-line' id='LC5'><span class="pl-c"><span class="pl-c">#</span> | Author: P4kL0nc4t &amp; Noxturnix</span></div><div class='line js-file-line' id='LC6'><span class="pl-c"><span class="pl-c">#</span> | Date: 25/04/2018</span></div><div class='line js-file-line' id='LC7'><span class="pl-c"><span class="pl-c">#</span> | Disclaimer: Editing author will not make you the real coder</span></div><div class='line js-file-line' id='LC8'><span class="pl-c"><span class="pl-c">#</span> | What&#39;s New?</span></div><div class='line js-file-line' id='LC9'><span class="pl-c"><span class="pl-c">#</span> | - Fixed 403 forbidden</span></div><div class='line js-file-line' id='LC10'><span class="pl-c"><span class="pl-c">#</span> | - Use less CPU</span></div><div class='line js-file-line' id='LC11'><br></div><div class='line js-file-line' id='LC12'><span class="pl-k">import</span> spammer_class</div><div class='line js-file-line' id='LC13'>spammer <span class="pl-k">=</span> spammer_class.Spammer()</div><div class='line js-file-line' id='LC14'>spammer.author <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>P4kL0nc4t &amp; Noxturnix<span class="pl-pds">&quot;</span></span></div><div class='line js-file-line' id='LC15'><span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;spammer.main()</div><div class='line js-file-line' id='LC17'><span class="pl-k">except</span> <span class="pl-c1">KeyboardInterrupt</span>:</div><div class='line js-file-line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> spammer_class.color.<span class="pl-c1">FAIL</span><span class="pl-k">+</span>spammer_class.color.<span class="pl-c1">REVERSE</span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\r</span>[!][except] KeyboardInterrupt detected! Exiting . . .<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>spammer_class.color.<span class="pl-c1">ENDC</span><span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span></div><div class='line js-file-line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">exit</span>()</div></pre></div></div>
    </div>
</div>


    <footer class="clearfix">
      <div class="container">
        <a href="#"><svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>

        <ul class="clearfix">
          <li>
            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-mobile-preference-form" action="/site/mobile_preference" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="r+B2S7fl4Jrjt9xbeKjE+OLvpG8wMZp/HnHO/s3MEMPS2v3a7l1LmW1D7bR+0F6JVoSK4Phhv4JdwgIt5f8DCg==" />
              <input type="hidden" name="mobile" value="false">
              <input type="hidden" name="anchor" class="js-mobile-preference-anchor-field">

              <button type="submit" class="switch-to-desktop" data-ga-click="Mobile, switch to desktop, switch button">
                Desktop version
              </button>
</form>          </li>
        </ul>
      </div>
    </footer>
  
    <script crossorigin="anonymous" async="async" integrity="sha512-PM87tD6azA5TJw6MI8Pbl6ZwFao5+bOf/RGq8GZ/mypHon7MVZiCYe9wA+C0xZSyD1yi8ARJkQuN/HjjEaYp6w==" type="application/javascript" src="https://github.githubassets.com/assets/mobile-bootstrap-5ee8948d.js"></script>

  </body>
</html>
