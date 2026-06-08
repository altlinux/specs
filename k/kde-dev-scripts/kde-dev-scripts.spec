%define rname kde-dev-scripts

%add_findreq_skiplist %_K6bin/kdedoc
%add_findreq_skiplist %_K6bin/package_crystalsvg
%add_findreq_skiplist %_K6bin/kde-systemsettings-tree.py
%filter_from_requires /^cvs$/d

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Various development scripts
Url: http://www.kde.org
License: BSD-2-Clause

BuildArch: noarch

Provides:  kde5-dev-scripts = %EVR
Obsoletes: kde5-dev-scripts < %EVR
Conflicts: colorsvn

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: graphviz perl-XML-DOM perl-podlators rpm-build-python rpm-build-python3 ruby ruby-stdlibs
BuildRequires: kf6-kdoctools kf6-kdoctools-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%K6install_move data uncrustify

# fix shebang
sed -i \
  -e "s|^#![[:space:]]*/usr/bin/env python$|#!%{__python3}|g" \
  %buildroot/%_K6bin/*

# fix scripts for strong /usr/lib/rpm/find-requires
for f in  %buildroot/%_K6bin/*
do
    file $f | grep -q shell || continue
    grep -q ^=head $f || continue
    mv "$f" "$f.tmp"
    awk 'BEGIN{found=0;} /^=head/ {if (found==0){print "cat <<\\__EOF__";found=1;};} {print} END{if (found!=0) print "__EOF__";}' <"$f.tmp" >"$f"
    rm -f "$f.tmp"
    chmod a+x $f
done


%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/* README
%_bindir/*
%_K6bin/*
%_K6data/uncrustify/


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Nov 01 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt2
- add conflict with colorsvn

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

