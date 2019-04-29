%define        pkgname nio4r

Name:          ruby-%pkgname
Version:       2.3.1
Release:       alt2
Summary:       New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/nio4r
# VCS:         https://github.com/socketry/nio4r.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API,
but simplified for ease-of-use. nio4r provides an abstract,
cross-platform stateful I/O selector API for Ruby. I/O selectors are the
heart of "reactor"-based event loops, and monitor multiple I/O objects
for various types of readiness, e.g. ready for reading or writing.


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
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
