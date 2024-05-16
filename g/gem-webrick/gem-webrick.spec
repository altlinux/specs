# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname webrick

Name:          gem-webrick
Version:       1.8.1
Release:       alt1
Summary:       WEBrick is an HTTP server toolkit that can be configured as an HTTPS server
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/webrick
Vcs:           https://github.com/ruby/webrick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(webrick) = 1.8.1


%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server.


%if_enabled    doc
%package       -n gem-webrick-doc
Version:       1.8.1
Release:       alt1
Summary:       WEBrick is an HTTP server toolkit that can be configured as an HTTPS server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webrick
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webrick) = 1.8.1

%description   -n gem-webrick-doc
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server
documentation files.
%description   -n gem-webrick-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webrick.
%endif


%if_enabled    devel
%package       -n gem-webrick-devel
Version:       1.8.1
Release:       alt1
Summary:       WEBrick is an HTTP server toolkit that can be configured as an HTTPS server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webrick
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webrick) = 1.8.1
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-webrick-devel
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server
development package.
%description   -n gem-webrick-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webrick.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-webrick-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-webrick-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- ^ 1.7.0 -> 1.8.1

* Fri Jan 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with usage Ruby Policy 2.0
