Name:		python-module-scripttest
Version:	1.0.4
Release:	alt1
Summary:	Helper to test command-line scripts

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/ScriptTest/
Source0:	%{name}-%{version}.tar.gz
# Issue preventing build and usage on ext4.
Patch0:		python-module-scripttest-1.0.4-files_updated.patch
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-nose

%description
ScriptTest is a library to help you test your interactive
command-line applications.

With it you can easily run the command (in a subprocess) and see
the output (stdout, stderr) and any file modifications.

%prep
%setup -q
%patch0 -p2 -b .files_updated

%build
%{__python} setup.py build

# generate docs
PYTHONPATH=./build/lib:$PYTHONPATH ./regen-docs
rm docs/_build/objects.inv
rm -rf docs/_build/.doctrees
rm docs/_build/.buildinfo
mv docs/_build docs/html

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
./test

%files
%defattr(-,root,root,-)
%doc docs/html
%doc docs/license.txt
%{python_sitelibdir}/scripttest/
%{python_sitelibdir}/ScriptTest*.egg-info

%changelog
* Sat Sep 15 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.4-alt1
- Initial release for Sisyphus (based on Fedora)
