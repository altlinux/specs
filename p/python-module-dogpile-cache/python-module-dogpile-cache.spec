%global modname dogpile.cache
%def_with python3

Name:               python-module-dogpile-cache
Version:            0.5.3
Release:            alt1
Summary:            A caching front-end based on the Dogpile lock

Group:              Development/Python
License:            BSD
URL:                http://pypi.python.org/pypi/dogpile.cache
Source0:            %{name}-%{version}.tar

BuildArch:          noarch

BuildRequires:      python-devel
BuildRequires:      python-module-setuptools
BuildRequires:      python-module-nose
BuildRequires:      python-module-mock
BuildRequires:      python-module-dogpile-core >= 0.4.1

Requires:           python-module-dogpile-core >= 0.4.1

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread generates
a new value.

dogpile.cache builds on the `dogpile.core
<http://pypi.python.org/pypi/dogpile.core>`_ locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract.   Overall, dogpile.cache is intended as a replacement to the
`Beaker <http://beaker.groovie.org>`_ caching system, the internals of
which are written by the same author.   All the ideas of Beaker which
"work" are re-implemented in dogpile.cache in a more efficient and succinct
manner, and all the cruft (Beaker's internals were first written in 2005)
relegated to the trash heap.

%if_with python3
%package -n python3-module-dogpile-cache
Summary:        A caching front-end based on the Dogpile lock
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-nose
BuildRequires:  python3-module-mock
BuildRequires:  python3-module-dogpile-core >= 0.4.1

Requires:       python3-module-dogpile-core >= 0.4.1

%description -n python3-module-dogpile-cache
dogpile.cache builds on the `dogpile.core
<http://pypi.python.org/pypi/dogpile.core>`_ locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract.   Overall, dogpile.cache is intended as a replacement to the
`Beaker <http://beaker.groovie.org>`_ caching system, the internals of
which are written by the same author.   All the ideas of Beaker which
"work" are re-implemented in dogpile.cache in a more efficient and succinct
manner, and all the cruft (Beaker's internals were first written in 2005)
relegated to the trash heap.

%endif

%prep
%setup

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE
%{python_sitelibdir}/dogpile/cache/
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-dogpile-cache
%doc README.rst LICENSE
%{python3_sitelibdir}/dogpile/cache/
%{python3_sitelibdir}/%{modname}-%{version}*
%endif

%changelog
* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.3-alt1
- First build for ALT (based on Fedora 0.5.3-3.fc21.src)

