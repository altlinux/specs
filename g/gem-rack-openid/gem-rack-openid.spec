%define        _unpackaged_files_terminate_build 1
%define        gemname rack-openid

Name:          gem-rack-openid
Version:       1.4.2.1
Release:       alt0.1
Summary:       Provides a more HTTPish API around the ruby-openid library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/rack-openid
Vcs:           https://github.com/grosser/rack-openid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-rg) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rack) >= 1.1.0
BuildRequires: gem(ruby-openid) >= 2.1.8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 1.1.0
Requires:      gem(ruby-openid) >= 2.1.8
Obsoletes:     ruby-rack-openid
Provides:      ruby-rack-openid
Provides:      gem(rack-openid) = 1.4.2.1

%ruby_use_gem_version rack-openid:1.4.2.1

%description
Provides a more HTTPish API around the ruby-openid library.


%package       -n gem-rack-openid-doc
Version:       1.4.2.1
Release:       alt0.1
Summary:       Provides a more HTTPish API around the ruby-openid library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-openid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-openid) = 1.4.2.1

%description   -n gem-rack-openid-doc
Provides a more HTTPish API around the ruby-openid library documentation files.

%description   -n gem-rack-openid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-openid.


%package       -n gem-rack-openid-devel
Version:       1.4.2.1
Release:       alt0.1
Summary:       Provides a more HTTPish API around the ruby-openid library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-openid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-openid) = 1.4.2.1
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-rg) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(bump) >= 0

%description   -n gem-rack-openid-devel
Provides a more HTTPish API around the ruby-openid library development package.

%description   -n gem-rack-openid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-openid.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rack-openid-doc
%ruby_gemdocdir

%files         -n gem-rack-openid-devel


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.2.1-alt0.1
- ^ 1.4.2 -> 1.4.2p1

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2.1
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt2
- used (>) Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus (without tests).
