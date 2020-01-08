%define        pkgname launchy
%define        apppkg ruby-launchy-app

Name:          ruby-%pkgname
Version:       2.4.3
Release:       alt3
Summary:       A helper for launching cross-platform applications in a fire and forget manner.
License:       ISC
Group:         Development/Ruby
Url:           https://github.com/copiousfreetime/launchy
%vcs           https://github.com/copiousfreetime/launchy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(simplecov)

%description
Launchy is helper class for launching cross-platform applications in a fire and
forget manner.

There are application concepts (browser, email client, etc) that are common
across all platforms, and they may be launched differently on each platform.
Launchy is here to make a common approach to launching external application from
within ruby programs.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %apppkg
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch
Obsoletes:     launchy <= 2.4.3-alt2
Conflicts:     launchy <= 2.4.3-alt2

%description   -n %apppkg
Executable file for %gemname gem.

%description   -n %apppkg -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         doc
%ruby_gemdocdir

%files         -n %apppkg
%_bindir/%{pkgname}*


%changelog
* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt3
- NMU: renamed launchy subpackage (closes: #37462)

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1.1
- Rebuild with new Ruby autorequirements.
- Package as gem.
- Package executable.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Initial build for Sisyphus
