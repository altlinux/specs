Name:    websocket-extensions-ruby
Version: 0.1.3
Release: alt1

Summary: Generic extension management for WebSocket connections
License: MIT
Group:   Development/Ruby
Url:     https://github.com/faye/websocket-extensions-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
A minimal framework that supports the implementation of WebSocket
extensions in a way that's decoupled from the main protocol. This
library aims to allow a WebSocket extension to be written and used with
any protocol library, by defining abstract representations of frames and
messages that allow modules to co-operate.

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus
