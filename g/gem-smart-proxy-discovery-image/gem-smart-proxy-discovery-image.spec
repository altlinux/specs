%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy_discovery_image

Name:          gem-smart-proxy-discovery-image
Version:       1.6.0
Release:       alt1.1
Summary:       FDI API for Foreman Smart-Proxy
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_discovery_image
Vcs:           https://github.com/theforeman/smart_proxy_discovery_image.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
BuildRequires: gem(smart_proxy) >= 0
%if_enabled check
BuildRequires: gem(json) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names smart_proxy_discovery_image,smart-proxy-discovery-image
Requires:      gem(smart_proxy) >= 0
Provides:      gem(smart_proxy_discovery_image) = 1.6.0

%description
Smart Proxy plugin providing Image API (reboot, kexec, facter) on discovered
nodes. This plugin is only useful on nodes booted into Foreman Discovery Image,
do not install it on regular Smart Proxy deployments: an enabled plugin makes
the host vulnerable to remote reboot and arbitrary code execution.


%if_enabled    doc
%package       -n gem-smart-proxy-discovery-image-doc
Version:       1.6.0
Release:       alt1.1
Summary:       FDI API for Foreman Smart-Proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_discovery_image
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_discovery_image) = 1.6.0

%description   -n gem-smart-proxy-discovery-image-doc
FDI API for Foreman Smart-Proxy documentation files.

Smart Proxy plugin providing Image API (reboot, kexec, facter) on discovered
nodes. This plugin is only useful on nodes booted into Foreman Discovery Image,
do not install it on regular Smart Proxy deployments: an enabled plugin makes
the host vulnerable to remote reboot and arbitrary code execution.

%description   -n gem-smart-proxy-discovery-image-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_discovery_image.
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-discovery-image-devel
Version:       1.6.0
Release:       alt1.1
Summary:       FDI API for Foreman Smart-Proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_discovery_image
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_discovery_image) = 1.6.0
Requires:      gem(json) >= 0

%description   -n gem-smart-proxy-discovery-image-devel
FDI API for Foreman Smart-Proxy development package.

Smart Proxy plugin providing Image API (reboot, kexec, facter) on discovered
nodes. This plugin is only useful on nodes booted into Foreman Discovery Image,
do not install it on regular Smart Proxy deployments: an enabled plugin makes
the host vulnerable to remote reboot and arbitrary code execution.

%description   -n gem-smart-proxy-discovery-image-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_discovery_image.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-smart-proxy-discovery-image-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-discovery-image-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Nov 11 2026 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1.1
- + declare the Smart Proxy host dependency
- * generate packaging and build from tagged sources

* Mon Nov 02 2026 Pavel Vasenkov <pav@altlinux.org> 1.6.0-alt1
- Initial build for ALT Linux Sisyphus (dependency of foreman-discovery-image).
