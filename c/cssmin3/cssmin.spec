%define _unpackaged_files_terminate_build 1

%define oname cssmin

Name:       %{oname}3
Version:    0.2.0
Release:    alt2
BuildArch:  noarch

License:    BSD
Group:      Development/Python3
Summary:    A Python port of the YUI CSS compression algorithm.

Url:        https://github.com/zacharyvoase/cssmin
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: python3-module-%oname


%description
A Python port of the YUI CSS compression algorithm.

%package -n python3-module-%oname
License:    BSD
Group:      Development/Python3
Summary:    Python3 module for cssmin.
BuildArch:  noarch

%description -n python3-module-%oname
A Python port of the YUI CSS compression algorithm.

Package contains python3 module for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

mv %buildroot/%_bindir/%oname %buildroot/%_bindir/%name

%files
%doc LICENSE README.*
%_bindir/%name

%files -n python3-module-%oname
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- porting on python3

* Mon Feb 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1
- Initial build
