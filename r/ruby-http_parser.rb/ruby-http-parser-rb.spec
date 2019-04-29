%define        pkgname http-parser-rb
%define        gemname http_parser.rb

Name: 	       ruby-%gemname
Version:       0.6.1
Release:       alt1
Summary:       A simple callback-based HTTP request/response parser for writing http servers, clients and proxies
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tmm1/http_parser.rb
# VCS:         https://github.com/tmm1/http_parser.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java

A simple callback-based HTTP request/response parser for writing http servers,
clients and proxies.

This gem is built on top of joyent/http-parser and its java port
http-parser/http-parser.java.


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
* Thu Apr 25 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- Move forward with sourcing from github
- Bump to 0.6.1
- Use Ruby Policy 2.0

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.5
- Rebuild for new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Rebuild with Ruby 2.3.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux
