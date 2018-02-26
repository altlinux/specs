%node_module daemon 0.5.1 1
Summary: Add-on for creating *nix daemons
Group: Development/Tools
Url: https://github.com/indexzero/daemon.node
License: MIT License
Source: module-source.tar
BuildRequires(pre): rpm-build-node

%description
This bindings provides all general connection/querying functions from MySQL C API,
and part of prepared statements support. `Connect`, `query` and `fetchAll` are asynchronous.
This module also includes experimental support for asynchronous `querySend` from internals of `libmysqlclient`.

%prep
%setup -q -n module-source

%build
%node_build
ln -s ../build/Release/daemon.node lib/daemon.v%node_version.node

%install
%node_install

%files
%doc README.md LICENSE examples
%node_modules/*

%changelog
* Thu Jun 21 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.5.1-alt4.1
- initial build


