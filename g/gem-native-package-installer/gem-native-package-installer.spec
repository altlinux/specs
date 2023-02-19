%define        gemname native-package-installer

Name:          gem-native-package-installer
Version:       1.1.5
Release:       alt1
Summary:       It helps to install native packages on "gem install"
License:       LGPL-3+
Group:         Development/Ruby
Url:           https://github.com/ruby-gnome2/native-package-installer
Vcs:           https://github.com/ruby-gnome2/native-package-installer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit-rr) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-native-package-installer < %EVR
Provides:      ruby-native-package-installer = %EVR
Provides:      gem(native-package-installer) = 1.1.5


%description
Users need to install native packages to install an extension library that
depends on native packages. It bores users because users need to install native
packages and an extension library separately. native-package-installer helps to
install native packages on "gem install". Users can install both native packages
and an extension library by one action, "gem install".


%package       -n gem-native-package-installer-doc
Version:       1.1.5
Release:       alt1
Summary:       It helps to install native packages on "gem install" documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета native-package-installer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(native-package-installer) = 1.1.5

%description   -n gem-native-package-installer-doc
It helps to install native packages on "gem install" documentation files.

Users need to install native packages to install an extension library that
depends on native packages. It bores users because users need to install native
packages and an extension library separately. native-package-installer helps to
install native packages on "gem install". Users can install both native packages
and an extension library by one action, "gem install".

%description   -n gem-native-package-installer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета native-package-installer.


%package       -n gem-native-package-installer-devel
Version:       1.1.5
Release:       alt1
Summary:       It helps to install native packages on "gem install" development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета native-package-installer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(native-package-installer) = 1.1.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit-rr) >= 0

%description   -n gem-native-package-installer-devel
It helps to install native packages on "gem install" development package.

Users need to install native packages to install an extension library that
depends on native packages. It bores users because users need to install native
packages and an extension library separately. native-package-installer helps to
install native packages on "gem install". Users can install both native packages
and an extension library by one action, "gem install".

%description   -n gem-native-package-installer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета native-package-installer.


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

%files         -n gem-native-package-installer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-native-package-installer-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- ^ 1.1.1 -> 1.1.5

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.7 -> 1.1.1

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt1
- Bump to 1.0.7
- Use Ruby Policy 2.0

* Sat Jan 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus
