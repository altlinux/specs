%global pypi_name Flask-XML-RPC-Re
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 0.1.4
Release: alt0.1
Summary: Adds support for creating XML-RPC APIs to Flask
Group: Development/Python3

License: MIT
Url: https://github.com/Croydon/flask-xml-rpc-reloaded
Source0: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python3

%description
This is a library that lets your Flask apps provide XML-RPC APIs. A small
example is included.

Flask-XML-RPC-Reloaded is a fork of the original Flask-XML-RPC, which was
unfortunately abandoned. This version should be 100%% compatible and therefore a
drop-in replacement for Flask-XML-RPC.

Differences to Flask-XML-RPC
- Python 3 support
- Uses the new Flask extension naming scheme

%description -n python3-module-%{pypi_name}
This is a library that lets your Flask apps provide XML-RPC APIs. A small
example is included.

Flask-XML-RPC-Reloaded is a fork of the original Flask-XML-RPC, which was
unfortunately abandoned. This version should be 100%% compatible and therefore a
drop-in replacement for Flask-XML-RPC.

Differences to Flask-XML-RPC
- Python 3 support
- Uses the new Flask extension naming scheme

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%python3_sitelibdir_noarch/flask_xmlrpcre
%python3_sitelibdir_noarch/flaskext
%python3_sitelibdir_noarch/Flask_XML_RPC_Re-%version.dist-info
%python3_sitelibdir_noarch/Flask_XML_RPC_Re-%version-*.pth

%changelog
* Thu Jan 25 2024 L.A. Kostis <lakostis@altlinux.ru> 0.1.4-alt0.1
- Initial build for ALTLinux.

