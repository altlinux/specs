%node_module mysql-libmysqlclient 1.3.3 1
Summary: Asynchronous MySQL binding for Node.js using libmysqlclient.
Group: Development/Tools
License: MIT License
Url: http://nodejs.org/
Source: module-source.tar
BuildRequires(pre): rpm-build-node
BuildRequires: libmysqlclient-devel

%description
This bindings provides all general connection/querying functions from MySQL C API,
and part of prepared statements support. `Connect`, `query` and `fetchAll` are asynchronous.
This module also includes experimental support for asynchronous `querySend` from internals of `libmysqlclient`.

%prep
%setup -q -n module-source

%build
%node_build
rm -rf tools

%install
%node_install

%files
%doc CHANGELOG.markdown README.markdown DEVELOPMENT.markdown AUTHORS doc
%node_modules/*

%changelog
* Thu Jun 21 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.3.3-alt4.1
- Rebuild with rpm-build-node

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.3.3-alt1
- initial


