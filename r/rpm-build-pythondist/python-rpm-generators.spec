Group: Development/Python3
%define _libexecdir %_prefix/libexec
%define oldname python-rpm-generators
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           rpm-build-pythondist
Summary:        Dependency generators for Python RPMs
Version:        14
Release:        alt1_8

Url:            https://src.fedoraproject.org/rpms/python-rpm-generators

# Originally the following files were part of RPM, so the license is inherited: GPL-2.0-or-later
# The COPYING file is grabbed from the last commit that changed the files
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
# This was crafted in-place as a fork of python.attr, hence also GPL-2.0-or-later
# This one is also originally from RPM, but it has its own license declaration: LGPL-2.1-or-later
Source4:        pythondistdeps.py
# This was crafted in-place with the following license declaration:
#  LicenseRef-Fedora-Public-Domain OR CC0-1.0 OR LGPL-2.1-or-later OR GPL-2.0-or-later
# Note that CC0-1.0 is not allowed for code in Fedora, so we skip it in the package License tag
Source5:        pythonbundles.py

# See individual licenses above Source declarations
# Originally, this was simplified to GPL-2.0-or-later, but "effective license" analysis is no longer allowed
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (LicenseRef-Fedora-Public-Domain OR LGPL-2.1-or-later OR GPL-2.0-or-later)

BuildArch:      noarch
Source44: import.info
BuildRequires: rpm-build-python3

%description
%{summary}.

%package -n rpm-build-python3dist
Group: Development/Python3
Summary:        %{summary}
Requires:       python3-module-packaging

%description -n rpm-build-python3dist
%{summary}.

%prep
%setup -n %{oldname}-%{version} -q -c -T

cp -a %{SOURCE0} %{SOURCE4} %{SOURCE5} .

%install
install -Dpm0755 -t %{buildroot}%{_libexecdir} *.py

#__pythondist_path ^/usr/lib(64)?/python[[:digit:]]\.[[:digit:]]+/site-packages/[^/]+\.(dist-info|egg-info|egg-link)$
cat > python3dist.prov.files <<'EOF'
#!/bin/gawk -f
BEGIN { FS = "\t" } ;
$1 ~ /\/usr\/lib(64)?\/python3(\.[[:digit:]]+)?\/site-packages\/[^/]+\.(dist-info|egg-info|egg-link)$/ { print $1 }
EOF

#__pythondist_provides  %{_libexecdir}/pythondistdeps.py --provides --normalized-names-format pep503 --package-name %{name} --normalized-names-provide-both --majorver-provides-versions 2.7,%%{__python3_version}
cat > python3dist.prov <<'EOF'
#!/bin/sh
exec %{_libexecdir}/pythondistdeps.py --provides --normalized-names-format pep503 --package-name $RPM_PACKAGE_NAME --normalized-names-provide-both --majorver-only
EOF

install -D -m755 python3dist.prov %buildroot%_rpmlibdir/python3dist.prov
install -D -m755 python3dist.prov.files %buildroot%_rpmlibdir/python3dist.prov.files

#no need for pythondist requires now
#__pythondist_requires  %{_libexecdir}/pythondistdeps.py --requires --normalized-names-format pep503 --package-name %{name} %%{?!_python_no_extras_requires:--require-extras-subpackages}


%files -n rpm-build-python3dist
%doc --no-dereference COPYING
%{_libexecdir}/pythondistdeps.py
%{_libexecdir}/pythonbundles.py

%_rpmlibdir/python3dist.prov
%_rpmlibdir/python3dist.prov.files


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 14-alt1_8
- update to new release by fcimport

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 14-alt1_7
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 14-alt1_3
- update to new release by fcimport

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 14-alt1_2
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 13-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 12-alt1_14
- update to new release by fcimport

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 12-alt1_13
- update to new release by fcimport

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 12-alt1_11
- update to new release by fcimport

* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 12-alt1_10
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 12-alt1_8
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 11-alt1_12
- update to new release by fcimport

* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 11-alt1_11
- new version

