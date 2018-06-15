Name:    websocket-driver-ruby
Version: 0.7.0
Release: alt1

Summary: WebSocket protocol handler with pluggable I/O
License: MIT
Group:   Development/Ruby
Url:     https://github.com/faye/websocket-driver-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%filter_from_requires \,^ruby(\(jruby\|websocket-driver/websocket_mask\)),d

%description
This module provides a complete implementation of the WebSocket
protocols that can be hooked up to any TCP library. It aims to simplify
things by decoupling the protocol details from the I/O layer, such that
users only need to implement code to stream data in and out of it
without needing to know anything about how the protocol actually works.
Think of it as a complete WebSocket system with pluggable I/O.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
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
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
