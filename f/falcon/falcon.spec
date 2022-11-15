%define _unpackaged_files_terminate_build 1

Name: falcon
Version: 1.4.1
Release: alt1.1

Summary: Framework for building high-performance microservices and app backends.
License: Apache-2.0
Group: Development/Python3
Url: https://falcon.readthedocs.io/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-mimeparse
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-jsonschema

Requires: python3-module-%name = %EVR
Requires: python3-module-django-dbbackend-sqlite3
Requires: python3-module-bottle
Requires: python3-module-flask
Requires: python3-module-werkzeug


%description
Falcon is a reliable, high-performance Python web framework for building 
large-scale app backends and microservices. It encourages the REST architectural
style, and tries to do as little as possible while remaining highly effective.

%package -n python3-module-%name
Summary: Framework for building high-performance microservices and app backends.
Group: Development/Python3
BuildArch: noarch

Requires: python3-module-six
Requires: python3-module-mimeparse

%description -n python3-module-%name
Falcon is a reliable, high-performance Python web framework for building 
large-scale app backends and microservices. It encourages the REST architectural
style, and tries to do as little as possible while remaining highly effective.

This package contain python modules for %name.

%add_python3_self_prov_path %buildroot%python3_sitelibdir/falcon/bench/

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.* LICENSE AUTHORS
%_bindir/falcon-bench
%_bindir/falcon-print-routes

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
