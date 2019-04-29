%define        pkgname websocket-driver
%define        gemname websocket-driver

Name:          %pkgname-ruby
Version:       0.7.0
Release:       alt2
Summary:       WebSocket protocol handler with pluggable I/O
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/faye/websocket-driver-ruby
# VCS:         https://github.com/faye/websocket-driver-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This module provides a complete implementation of the WebSocket
protocols that can be hooked up to any TCP library. It aims to simplify
things by decoupling the protocol details from the I/O layer, such that
users only need to implement code to stream data in and out of it
without needing to know anything about how the protocol actually works.
Think of it as a complete WebSocket system with pluggable I/O.

%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-ruby-doc
Provides:      %pkgname-ruby-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%prep
%setup

%build
%gem_build --alias=websocket-driver:websocket-driver-ruby --join=bin:lib

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemextdir
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
