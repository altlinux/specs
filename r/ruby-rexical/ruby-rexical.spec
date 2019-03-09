%define        pkgname rexical

Name:          ruby-%pkgname
Version:       1.0.5
Release:       alt4.gitd8af06b89
Summary:       Lexical scanner generator for ruby
Group:         Development/Ruby
License:       LGPL
Url:           https://github.com/tenderlove/rexical
# VCS:         https://github.com/tenderlove/rexical.git
BuildArch:     noarch
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-hoe
Conflicts: rex

%description
Rexical is a lexical scanner generator. It is written in Ruby itself,
and generates Ruby program. It is designed for use with Racc.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%files
%_bindir/*
%ruby_gemspec
%ruby_gemlibdir/*

%files         doc
%ruby_gemdocdir/*

%changelog
* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt4.gitd8af06b89
- Use Ruby Policy 2.0;
- Use latest git commit.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt3.1
- Rebuild with new Ruby autorequirements.

* Thu Dec 13 2012 Led <led@altlinux.ru> 1.0.5-alt3
- rename %%_bindir/rex -> %%_bindir/rexical for avoid file conflict
  with (R)?ex (rex package)
- fixed BuildRequires

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.0.5-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt2
- Pick off rubygems.

* Thu Mar 24 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt1
- [1.0.5]
