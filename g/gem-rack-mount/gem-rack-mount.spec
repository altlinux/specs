%define        _unpackaged_files_terminate_build 1
%define        gemname rack-mount

Name:          gem-rack-mount
Version:       0.8.3.13
Release:       alt0.1
Summary:       Stackable dynamic tree based Rack router
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sporkmonger/rack-mount
Vcs:           https://github.com/sporkmonger/rack-mount.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rexical) >= 0
BuildRequires: gem(rack) >= 1.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 1.0.0
Provides:      gem(rack-mount) = 0.8.3.13

%ruby_use_gem_version rack-mount:0.8.3.13

%description
A stackable dynamic tree based Rack router.

Rack::Mount supports Rack's X-Cascade convention to continue trying routes if
the response returns pass. This allows multiple routes to be nested or stacked
on top of each other. Since the application endpoint can trigger the router to
continue matching, middleware can be used to add arbitrary conditions to any
route. This allows you to route based on other request attributes, session
information, or even data dynamically pulled from a database.


%package       -n gem-rack-mount-doc
Version:       0.8.3.13
Release:       alt0.1
Summary:       Stackable dynamic tree based Rack router documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-mount
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-mount) = 0.8.3.13

%description   -n gem-rack-mount-doc
Stackable dynamic tree based Rack router documentation files.

A stackable dynamic tree based Rack router.

Rack::Mount supports Rack's X-Cascade convention to continue trying routes if
the response returns pass. This allows multiple routes to be nested or stacked
on top of each other. Since the application endpoint can trigger the router to
continue matching, middleware can be used to add arbitrary conditions to any
route. This allows you to route based on other request attributes, session
information, or even data dynamically pulled from a database.

%description   -n gem-rack-mount-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-mount.


%package       -n gem-rack-mount-devel
Version:       0.8.3.13
Release:       alt0.1
Summary:       Stackable dynamic tree based Rack router development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-mount
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-mount) = 0.8.3.13
Requires:      gem(racc) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rexical) >= 0

%description   -n gem-rack-mount-devel
Stackable dynamic tree based Rack router development package.

A stackable dynamic tree based Rack router.

Rack::Mount supports Rack's X-Cascade convention to continue trying routes if
the response returns pass. This allows multiple routes to be nested or stacked
on top of each other. Since the application endpoint can trigger the router to
continue matching, middleware can be used to add arbitrary conditions to any
route. This allows you to route based on other request attributes, session
information, or even data dynamically pulled from a database.

%description   -n gem-rack-mount-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-mount.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rack-mount-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-rack-mount-devel
%doc README.rdoc


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.3.13-alt0.1
- ^ 0.8.3 -> 0.8.3p13

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt2
- used (>) Ruby Policy 2.0
- fixed (!) spec minorly

* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus, packaged as gem
