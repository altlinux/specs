%def_with python3

Name: suid-python
Version: 0.95
Release: alt1
Summary: This is a setuid wrapper for Python scripts
License: Python
Group: Development/Python
Url: http://selliott.org/python/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
A program to securely run Python scripts with the setuid bits set on the
script applied to the resulting Python process as if the Python script
was an executable. This utility could probably be easily adapted to
other scripting languages.

%package -n %{name}3
Summary: This is a setuid wrapper for Python scripts
Group: Development/Python3

%description -n %{name}3
A program to securely run Python scripts with the setuid bits set on the
script applied to the resulting Python process as if the Python script
was an executable. This utility could probably be easily adapted to
other scripting languages.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|#define PYTHON "python"|#define PYTHON "python3"|' \
	../python3/%name.c
%endif

%build
gcc %optflags -o %name %name.c

%if_with python3
pushd ../python3
gcc %optflags -o %{name}3 %name.c
popd
%endif

%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir/
chmod u+s %buildroot%_bindir/%name

%if_with python3
pushd ../python3
install -m755 %{name}3 %buildroot%_bindir/
chmod u+s %buildroot%_bindir/%{name}3
popd
%endif

%files
%_bindir/%name

%if_with python3
%files -n %{name}3
%_bindir/%{name}3
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Initial build for Sisyphus

