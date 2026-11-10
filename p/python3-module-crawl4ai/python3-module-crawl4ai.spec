%define pypi_name crawl4ai

Name: python3-module-crawl4ai
Version: 0.9.5
Release: alt1
Summary: Asynchronous web crawler and scraper

License: Apache-2.0
Group: Development/Python3
URL: https://github.com/unclecode/crawl4ai
# Source-url: https://github.com/unclecode/crawl4ai/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: crawl4ai.service
Source2: crawl4ai.sysusers.conf
Source3: crawl4ai-server
Source4: crawl4ai.sysconfig
Patch1: 0001-browser-executable-path.patch
Patch2: 0002-system-chromium-only.patch
Patch3: 0003-optional-features.patch
Patch4: 0004-server-config-path.patch
Patch5: 0005-runtime-dependencies.patch
Patch6: 0006-mcp2.patch
Patch7: 0007-sisyphus-requirements.patch
# System Chromium is unavailable on i586.
ExcludeArch: %ix86
# Optional features import these only when explicitly selected. No LLM/ML stack
# or alternate browser is needed to render and extract ordinary web pages.
%add_python3_req_skip litellm litellm.exceptions torch transformers sklearn scipy spacy tiktoken
%add_python3_req_skip patchright.async_api playwright_stealth selenium
# Private server modules resolve from the script directory, not site-packages.
%add_findprov_skiplist %python3_sitelibdir/crawl4ai_server/*
%add_python3_req_skip api artifacts auth auth_gate crawler_pool egress_broker egress_proxy
%add_python3_req_skip governor hook_registry job llm_broker mcp_bridge monitor monitor_routes
%add_python3_req_skip redis_config schemas utils webhook work_queue
Requires: /usr/bin/chromium
BuildRequires(pre): rpm-macros-python3 rpm-macros-systemd
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel

%description
Crawl4AI is an asynchronous web crawler that extracts structured data and
Markdown from web pages using a browser.

%package -n crawl4ai
Summary: Command line interface for the Crawl4AI web crawler

Group: Networking/WWW
Requires: %name = %EVR

%description -n crawl4ai
Command line crawling, configuration, browser diagnostics and cache migration.
Setup checks the system Chromium; it does not install browsers.

%package -n crawl4ai-server
Summary: REST service for asynchronous web crawling

Group: Networking/WWW
Requires: %name = %EVR
Requires: /usr/bin/redis-server

%description -n crawl4ai-server
Crawl4AI REST server with Markdown, HTML, crawl and screenshot endpoints.
The service listens on 127.0.0.1 by default and runs as a dedicated user.
Redis provides background task and monitoring storage.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%pyproject_build

%install
%pyproject_install --platlib
install -d %buildroot%python3_sitelibdir/crawl4ai_server
install -m644 deploy/docker/*.py deploy/docker/c4ai-*-context.md %buildroot%python3_sitelibdir/crawl4ai_server/
cp -a deploy/docker/static %buildroot%python3_sitelibdir/crawl4ai_server/
install -Dm644 deploy/docker/config.yml %buildroot%_sysconfdir/crawl4ai/config.yml
install -Dm644 %SOURCE1 %buildroot%_unitdir/crawl4ai.service
install -Dm644 %SOURCE2 %buildroot%_sysusersdir/crawl4ai.conf
install -Dm755 %SOURCE3 %buildroot%_bindir/crawl4ai-server
sed -i 's|@SERVER_DIR@|%python3_sitelibdir/crawl4ai_server|' %buildroot%_bindir/crawl4ai-server
# Give the private server modules a namespace for automatic RPM dependencies.
touch %buildroot%python3_sitelibdir/crawl4ai_server/__init__.py
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/crawl4ai
# Upstream's test websocket client is not server runtime code.
rm -f %buildroot%python3_sitelibdir/crawl4ai_server/test-websocket.py

%pre -n crawl4ai-server
%sysusers_create_package crawl4ai %SOURCE2

%post -n crawl4ai-server
%post_systemd crawl4ai.service

%preun -n crawl4ai-server
%preun_systemd crawl4ai.service

%files
%python3_sitelibdir/crawl4ai/
%python3_sitelibdir/%{pyproject_distinfo Crawl4AI}/
%doc README.md LICENSE

%files -n crawl4ai
%_bindir/crwl
%_bindir/crawl4ai-setup
%_bindir/crawl4ai-doctor
%_bindir/crawl4ai-migrate

%files -n crawl4ai-server
%_bindir/crawl4ai-server
%python3_sitelibdir/crawl4ai_server/
%_unitdir/crawl4ai.service
%_sysusersdir/crawl4ai.conf
%config(noreplace) %_sysconfdir/crawl4ai/config.yml
%config(noreplace) %_sysconfdir/sysconfig/crawl4ai

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- initial build for ALT Sisyphus
- build architecture-dependent packages; exclude i586.

