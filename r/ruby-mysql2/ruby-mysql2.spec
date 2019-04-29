%define        pkgname mysql2

Name: 	       ruby-%pkgname
Version:       0.5.2
Release:       alt2
Summary:       A modern, simple and very fast Mysql library for Ruby - binding to libmysql
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/mysql2
# VCS:         https://github.com/brianmario/mysql2.git

Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libmysqlclient-devel

%description
The Mysql2 gem is meant to serve the extremely common use-case of
connecting, querying and iterating on results. Some database libraries
out there serve as direct 1:1 mappings of the already complex C APIs
available. This one is not.

It also forces the use of UTF-8 [or binary] for the connection [and all
strings in 1.9, unless Encoding.default_internal is set then it will
convert from UTF-8 to that encoding] and uses encoding-aware MySQL API
calls where it can.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup

%build
%gem_build
#%ruby_config -- --without-mysql-rpath

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt2
- Use Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- New version.
- Package as gem.

* Wed Apr 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with Ruby 2.5.1

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt2
- Rebuild with new %%ruby_sitearchdir location

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.5-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt2
- Rebuild with Ruby 2.3.1

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.18-alt1
- Initial build for ALT Linux
