#%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Name:		python-module-qpid
Version:	0.18
Release:	alt1
Summary:	Python client library for AMQP

License:	ASL 2.0
Group:		Development/Python
URL:		http://qpid.apache.org
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python-devel

%description
The Apache Qpid Python client library for AMQP.

%prep
%setup -q -n %{name}-%{version}/python
cd ..

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %buildroot

chmod +x %{buildroot}/%{python_sitelibdir}/qpid/codec.py
chmod +x %{buildroot}/%{python_sitelibdir}/qpid/tests/codec.py
chmod +x %{buildroot}/%{python_sitelibdir}/qpid/reference.py
chmod +x %{buildroot}/%{python_sitelibdir}/qpid/managementdata.py
chmod +x %{buildroot}/%{python_sitelibdir}/qpid/disp.py

%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt README.txt examples
%{python_sitelibdir}/mllib
%{python_sitelibdir}/qpid
%{_bindir}/qpid-python-test

%if "%{python_version}" >= "2.6"
%{python_sitelibdir}/qpid_python-*.egg-info
%endif

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.18-alt1
- Initial release for Sisyphus (based on Fedora)
