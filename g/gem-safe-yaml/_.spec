%define        pkgname safe-yaml
%define        gemname safe_yaml

Name:          gem-%pkgname
Version:       1.0.5
Release:       alt2
Summary:       Parse YAML safely
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dtao/safe_yaml
%vcs           https://github.com/dtao/safe_yaml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
Obsoletes:     ruby-%gemname
Provides:      ruby-%gemname

%description
%summary.

%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Obsoletes:     %gemname
Provides:      %gemname

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Obsoletes:     ruby-%gemname-doc
Provides:      ruby-%gemname-doc

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{gemname}*

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2
- + obsoleting ruby-self_yaml package

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
