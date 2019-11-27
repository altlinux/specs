%define   pypi_name power

Name:           python3-module-%{pypi_name}
Version:        1.4
Release:        alt2

Summary:        Cross-platform system power status information
License:        MIT
Group:          Development/Python3
URL:            https://github.com/Kentzo/Power
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires(pre): rpm-build-python3


%description
Python module that allows you to get power and battery status of the
system.

%prep
%setup -q

# Remove Mac-specific file
rm -f power/darwin.py

find ./ -name '*.py' | xargs sed -i '1s|^#!%{__python}|#!%{__python3}|'

%build
%python3_build

%install
%python3_install

%check
%__python3 -m unittest -v power.tests

%files
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt1.1
- (NMU) rebuild with python3.6

* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Initail build in Sisyphus

