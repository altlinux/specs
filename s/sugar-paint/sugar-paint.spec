# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define fedora 18
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           sugar-paint
Version:        43
Release:        alt1_1
Summary:        Paint activity for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2
URL:            http://wiki.sugarlabs.org/go/Activities/Paint
Source0:        http://download.sugarlabs.org/sources/honey/Paint/Paint-%{version}.tar.bz2
Patch0:         sugar-paint-Fedora.patch
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  python-module-pygtk-devel
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit
Requires:       sugar
Source44: import.info

%description
Paint will provide a canvas for an individual or a group of children 
to express themselves creatively through drawing. 

%prep
%setup -q -n Paint-%{version}

# make sure to grab blob from the right location and remove prebuilt ones
sed '49,53d' -i fill/Makefile
rm -rf fill/linux*
%patch0 -p1 -b .fedora

%build
make %{?_smp_mflags} V=1 -C fill LDFLAGS+=--build-id
%{__python} ./setup.py build

%install
mkdir -p %{buildroot}%{python_sitelibdir}/fill/
install -Dm 0755 fill/lib/_fill.so %{buildroot}%{python_sitelibdir}/fill/
install -Dm 0644 fill/lib/__init__.py %{buildroot}%{python_sitelibdir}/fill/
%{__python} setup.py install --prefix=%{buildroot}/%{_prefix}
rm -rf %{buildroot}%{sugaractivitydir}Paint.activity/fill
%find_lang org.laptop.Oficina

%files -f org.laptop.Oficina.lang
%doc NEWS COPYING
%{python_sitelibdir}/fill/
%{sugaractivitydir}/Paint.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 43-alt1_1
- new version; import from fc17 updates

