%define _unpackaged_files_terminate_build 1

%def_with check

Name: falcon
Version: 4.0.2
Release: alt1

Summary: Fast ASGI+WSGI framework for building data plane APIs at scale
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/falcon
Vcs: https://github.com/falconry/falcon
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-requests
BuildRequires: python3-module-cbor2
BuildRequires: python3-module-httpx
BuildRequires: python3-module-websockets
BuildRequires: python3-module-aiofiles
%endif

Requires: python3-module-%name = %EVR

%description
Falcon is a reliable, high-performance Python web framework for building
large-scale app backends and microservices. It encourages the REST architectural
style, and tries to do as little as possible while remaining highly effective.

%package -n python3-module-%name
Summary: Fast ASGI+WSGI framework for building data plane APIs at scale
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
Falcon is a reliable, high-performance Python web framework for building
large-scale app backends and microservices. It encourages the REST architectural
style, and tries to do as little as possible while remaining highly effective.

This package contain python modules for %name.

%add_python3_self_prov_path %buildroot%python3_sitelibdir/falcon/bench/

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.* LICENSE AUTHORS
%_bindir/falcon-bench
%_bindir/falcon-print-routes
%_bindir/falcon-inspect-app

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info


%changelog
* Fri Dec 13 2024 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1.2
- NMU: Added zombie-imp to BuildRequires.

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
