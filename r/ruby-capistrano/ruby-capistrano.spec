%define        pkgname capistrano

Name:          ruby-%pkgname
Version:       3.11.0
Release:       alt1
Summary:       Capistrano -- Welcome to easy deployment with Ruby over SSH
Group:         Development/Ruby
License:       MIT
Url:           https://capistranorb.com/
# VCS:         https://github.com/capistrano/capistrano.git
BuildArch:     noarch
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Capistrano is a framework for building automated deployment scripts. Although
Capistrano itself is written in Ruby, it can easily be used to deploy projects
of any language or framework, be it Rails, Java, or PHP.

%package       doc
Summary: Documentation files for %name
Group: Documentation

%description   doc
Documentation files for %name.

%package       -n cap
Summary:       Documentation files for %name
Group:         Development/Tools

%description   -n cap
Capistrano gives you a cap tool to perform your deployments from the comfort of
your command line.

%prep
%setup -q -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemlibdir/*

%files         -n cap
%_bindir/*

%files         doc
%ruby_gemdocdir/*

%changelog
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

