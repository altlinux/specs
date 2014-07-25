Name:           python-module-oslo-rootwrap
Version:        1.0.0
Release:        alt1
Summary:        Oslo Rootwrap

Group:		Development/Python
License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr


%description
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

Unlike other Oslo deliverables, it should **not** be used as a Python library,
but called as a separate process through the `oslo-rootwrap` command:

`sudo oslo-rootwrap ROOTWRAP_CONFIG COMMAND_LINE`

%prep
%setup
# Remove bundled egg-info
#rm -rf %%{pypi_name}.egg-info

%build
%python_build


%install
%python_install

#%check
#%{__python} setup.py test

%files
%doc README.rst LICENSE
%{_bindir}/oslo-rootwrap
%dir %{python_sitelibdir}/oslo
%{python_sitelibdir}/oslo/rootwrap
%{python_sitelibdir}/oslo.rootwrap-%{version}*

%changelog
* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Matthias Runge <mrunge@redhat.com> - 1.0.0-1
- Initial package.
