Name: apoo
Version: 2.2
Release: alt1
License: GPLv2
Summary: An Assembly course aid
Group: Education
BuildArch: noarch
Url: http://www.ncc.up.pt/Apoo/
Source: %{name}_%version.orig.tar.gz

Patch0: 0001-apoo-2.2-alt.patch

%setup_python_module %name
Requires: %packagename = %version

%description
A virtual machine (a CPU) created for teaching purposes. All the programs
are written in Python and are very easy to extend to incorporate new
assembly-like pseudo-instuctions. A gtk2-based interface is provided, to
help debugging or just examining the execution of programs.
Another program permits a tutor to create exercises and write rules to
automatically grade the students' solutions.

%package -n %packagename
Summary: Supplemental module for %name, %summary
Group: Education
%description -n %packagename
%summary

%prep
%setup
sed -i '
s@%%_defaultdocdir@%_defaultdocdir@g
s@%%python_sitelibdir_noarch@%python_sitelibdir_noarch@g
s@%%name@%name@g
s@%%version@%version@g
' %PATCH0
%patch0 -p2

%build
%install
install -D exec-apoo.master %buildroot%_bindir/exec-apoo
install -D -m644 /dev/null %buildroot%python_sitelibdir_noarch/apoo/__init__.py
install *.py %buildroot%python_sitelibdir_noarch/apoo/
ln -s `realpath --relative-to=%buildroot%_bindir %buildroot%python_sitelibdir_noarch/apoo/interface.py` %buildroot%_bindir/%name
ln -s `realpath --relative-to=%buildroot%_bindir %buildroot%python_sitelibdir_noarch/apoo/vpu_tutor.py` %buildroot%_bindir/%name-tutor

%files
%doc docs/* html examples
%_bindir/*

%files -n %packagename
%python_sitelibdir_noarch/%name

%changelog
* Tue Sep 11 2012 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Tue Sep 11 2012 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial zero version build from scratch

