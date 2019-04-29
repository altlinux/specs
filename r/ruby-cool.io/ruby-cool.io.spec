%define        pkgname cool-io
%define        gemname cool.io

Name:          ruby-%gemname
Version:       1.5.4
Release:       alt1
Summary:       Simple evented I/O for Ruby (but please check out Celluloid::IO instead)
License:       MIT
Group:         Development/Ruby
Url:           https://coolio.github.io/
# VCS:         https://github.com/tarcieri/cool.io.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

Cool.io is an event library for Ruby, built on the libev event library, which
provides a cross-platform interface to high performance system calls. This
includes the epoll system call for Linux, the kqueue system call for BSDs and
OS X, and the completion ports interface for Solaris.

Cool.io also binds asynchronous wrappers to Ruby's core socket classes so you
can use them in conjunction with Cool.io to build asynchronous event-driven
applications.


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
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- Bump to 1.5.4
- Use Ruby Policy 2.0

* Sat Sep 29 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.3-alt1
- Initial build for Sisyphus
