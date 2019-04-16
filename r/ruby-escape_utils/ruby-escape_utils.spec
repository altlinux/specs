%define        pkgname escape-utils
%define        gemname escape_utils

Name: 	       ruby-%gemname
Version:       1.2.1 
Release:       alt2
Summary:       Faster string escaping routines for your ruby apps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/escape_utils
# VCS:         https://github.com/brianmario/escape_utils.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Being as though we're all html escaping everything these days, why not make it
faster?

For character encoding in 1.9, the output string's encoding is copied from
the input string.

It has monkey-patches for Rack::Utils, CGI, URI, ERB::Util and Haml and
ActionView so you can drop this in and have your app start escaping fast as
balls in no time

It supports HTML, URL, URI and Javascript escaping/unescaping.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%gemname-doc
Obsoletes:     ruby-%gemname-doc

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
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt2
- Use Ruby Policy 2.0

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.5
- Build for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
