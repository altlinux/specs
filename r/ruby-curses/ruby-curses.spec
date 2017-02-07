%define  pkgname curses
 
Name: 	 ruby-%pkgname
Version: 1.1.2
Release: alt1
 
Summary: Ruby binding for curses, ncurses, and PDCurses
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ruby/curses
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libncursesw-devel
 
%filter_from_requires /^ruby(#.*\/curses.so)/d

%description
A Ruby binding for curses, ncurses, and PDCurses. curses is an extension
library for text UI applications.  Formerly part of the Ruby standard
library.

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%changelog
* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build in Sisyphus
