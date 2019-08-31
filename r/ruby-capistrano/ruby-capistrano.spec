%define        pkgname capistrano

Name:          ruby-%pkgname
Version:       3.11.0
Release:       alt1.1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH
Group:         Development/Ruby
License:       MIT
Url:           https://capistranorb.com/
%vcs           https://github.com/capistrano/capistrano.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.


%package       -n cap
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n cap
Executable file for %gemname gem.

%description   -n cap -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=docs

%install
%ruby_install

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n cap
%_bindir/cap*

%files         doc
%ruby_gemdocdir

%changelog
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.0-alt1.1
- Fix spec

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.0-alt1
- Bump to 3.11.0;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.10-alt1.2
- Rebuild with Ruby 2.4.1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.5.10-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.5.10-alt1
- build for Sisyphus

