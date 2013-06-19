# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/python pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
# The git_commit define will have the complement given by git-hub to the source downloaded
%define git_commit fadf11e
Name:           libcwiid
Version:        0.6.00
Release:        alt2.20100505git%{git_commit}
Summary:        Wiimote interface library

Group:          System/Libraries
License:        GPLv2+
URL:            http://abstrakraft.org/cwiid/
Packager:       Andrey Cherepanov <cas@altlinux.org>

# source URL : http://github.com/abstrakraft/cwiid/tarball/%%{git_commit} 
Source0:        abstrakraft-cwiid-%{git_commit}.tar.gz
Source1:        wmgui.desktop

# this patch is in my git-hub fork git://github.com/bogado/cwiid.git
# there is an upstream bug filed by me at http://abstrakraft.org/cwiid/ticket/105
Patch0:         0001-Fix-missing-library-from-wmdemo.patch

BuildRequires:  libbluez-devel gawk bison flex gtk2-devel python-devel >= 2.4 desktop-file-utils
Source44: import.info

%description
Cwiid is a library that enables your application to communicate with
a wiimote using a bluetooth connection.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python-module-cwiid
Summary:        Python binding for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    -n python-module-cwiid
Python2 binding for %{name}

%package        utils
Summary:        Wiimote connection test application
Group:          File tools
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-wmgui = %{version}-%{release}
Obsoletes:      %{name}-wmgui < 0.6.00-7

%description    utils
Applications to test the wiimote connection

%package        wminput
Summary:        Enables using the wiimote as an input source
# The licence must be GPLv2 instead of GPLv2+ for this package
# since the file wminput/action_enum.txt is GPLv2 as stated
# in the file.
License:        GPLv2
Group:          File tools
Requires:       %{name} = %{version}-%{release}

%description    wminput
This program allows the user to use the wiimote to emulate normal system
input sources like the mouse and keyboard.

%prep
%setup -q -n abstrakraft-cwiid-%{git_commit}
%patch0 -p1

%build
aclocal
autoconf
%configure CC="gcc %{optflags}" --disable-static
make %{?_smp_mflags}

%install
%makeinstall_std LDCONFIG=/bin/true
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# find all directories 
find $RPM_BUILD_ROOT%{_sysconfdir} -type f -exec chmod 0644 {} ';'
rm $RPM_BUILD_ROOT/%{_libdir}/*.a
desktop-file-install --dir=%buildroot%_desktopdir %{SOURCE1}

%files
%doc AUTHORS NEWS README COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_pkgconfigdir}/*

%files -n python-module-cwiid
%{python_sitelibdir}/*

%files wminput
%config(noreplace) %{_sysconfdir}/cwiid/
%{_bindir}/wminput
%{_man1dir}/wminput*
%{_libdir}/cwiid
%{_defaultdocdir}/cwiid

%files utils
%{_bindir}/lswm
%{_bindir}/wmgui
%{_man1dir}/wmgui*
%{_desktopdir}/wmgui.desktop

%changelog
* Wed Jun 19 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.00-alt2.20100505gitfadf11e
- Initial import to Sisypus from autoimports
- Rename to libcwiid according to ALT Linux policy

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.00-alt1_21.20100505gitfadf11e
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.00-alt1_20.20100505gitfadf11e
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.00-alt1_19.20100505gitfadf11e
- update to new release by fcimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.00-alt1_18.20100505gitfadf11e
- fc import

