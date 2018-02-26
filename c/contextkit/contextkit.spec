Name:       contextkit
Summary:    Contextual information collection framework
Version:    0.5.27
Release:    alt1.427.1
Group:      System/Libraries
License:    GPLv2
URL:        http://maemo.gitorious.org/maemo-af/%{name}
Source0:    %{name}-%{version}.tar.bz2
Source100:  contextkit.yaml
Patch0:     contextkit-gcc45.patch
#Requires(post): /sbin/ldconfig
#Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QJson)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  asciidoc
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  perl-XML-DOM
BuildRequires:  python
BuildRequires:  tinycdb-devel
BuildRequires:  rpm-build-python
BuildRequires:  xsltproc
BuildRequires:  gcc-c++


%description
This is ContextKit, a framework for collecting contextual information from
the bowels of the system, cleaning them up and offering them through a simple
API.

The ContextKit consists of:
* libcontextprovider, a convenience library to export contextual properties
  to the rest of the system.
* user documentation including a list of standard context properties.
* contextd, daemon for combining and refining contextual information.
* libcontextsubscriber, a library implementing the simple API for accessing
  the contextual information.



%package devel
Summary:    Development files for ContextKit APIs
Group:      Development/C++
Requires:   %{name} = %{version}-%{release}

%description devel
Development libraries and headers for building context aware applications.


%package doc
Summary:    Documentation for ContextKit APIs
Group:      Documentation
BuildArch:    noarch
Requires:   %{name} = %{version}-%{release}

%description doc
This package contains the ContextKit documentation.


%package -n python-%{name}
Summary:    Python bindings for ContextKit APIs
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n python-%{name}
This package contains Python bindings for the libcontextprovider
C interface, which helps you writing providers in Python.


%package tests
Summary:    ContextKit automated customer tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   python-%{name} = %{version}-%{release}

%description tests
This package contains an automated customer testsuite of the
ContextKit libraries.



%prep
%setup -q -n %{name}-%{version}

# contextkit-gcc45.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

#./autogen.sh --disable-static
%autoreconf
%configure
%make_build

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%makeinstall_std pythondir=%python_sitelibdir

# >> install post
# Fix rpmlint non-executable-script warning
chmod 0755 %{buildroot}%python_sitelibdir/ContextKit/flexiprovider.py
chmod 0755 %{buildroot}%python_sitelibdir/ContextKit/cltool.py
# << install post

mkdir -m0755 -p %{buildroot}%{_datadir}/%name/providers
mkdir -m0755 -p %{buildroot}%{_datadir}/%name/subscribers

#%post -p /sbin/ldconfig

#%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/dbus-1/system.d/libcontextprovider0.conf
%{_bindir}/update-%{name}-providers
%{_libdir}/libcontextprovider.so.*
%{_libdir}/libcontextsubscriber.so.*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%name
%dir %{_datadir}/%name/providers
%dir %{_datadir}/%name/subscribers
%{_datadir}/%{name}/core.context
%dir %{_datadir}/%name/types
%{_datadir}/%{name}/types/core.types
%doc %{_mandir}/man1/update-%{name}-providers.*
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/contextprovider
%{_includedir}/contextprovider/*
%dir %{_includedir}/contextsubscriber
%{_includedir}/contextsubscriber/*
%{_libdir}/libcontextprovider.so
%{_libdir}/libcontextsubscriber.so
%{_libdir}/pkgconfig/contextprovider-1.0.pc
%{_libdir}/pkgconfig/contextsubscriber-1.0.pc
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-doc
%dir %{_docdir}/%{name}-doc/html
%doc %{_docdir}/%{name}-doc/html/*.html
%doc %{_docdir}/%{name}-doc/html/*.png
# >> files doc
# << files doc

%files -n python-%{name}
%defattr(-,root,root,-)
%{_bindir}/context-rlwrap
%dir %python_sitelibdir/ContextKit
%python_sitelibdir/ContextKit/*.py
%python_sitelibdir/ContextKit/*.pyc
%python_sitelibdir/ContextKit/*.pyo
# >> files python-%{name}
# << files python-%{name}

%files tests
%defattr(-,root,root,-)
%{_bindir}/check-version
%{_bindir}/context-listen
%{_bindir}/context-ls
%{_bindir}/context-provide
%dir %{_libdir}/%{name}/subscriber-test-plugins
%{_libdir}/%{name}/subscriber-test-plugins/contextsubscribertime*.so
%exclude %{_libdir}/%{name}/subscriber-test-plugins/contextsubscribertime*.la
%dir %{_libdir}/libcontextprovider-tests
%{_libdir}/libcontextprovider-tests/*
%dir %{_libdir}/libcontextsubscriber-tests
%{_libdir}/libcontextsubscriber-tests/*
%dir %{_datadir}/libcontextprovider-tests
%{_datadir}/libcontextprovider-tests/tests.xml
%dir %{_datadir}/libcontextsubscriber-tests
%{_datadir}/libcontextsubscriber-tests/tests.xml
%dir %{_datadir}/libcontextsubscriber-tests/waitforsubscription
%{_datadir}/libcontextsubscriber-tests/waitforsubscription/context-provide.context
%doc %{_mandir}/man1/context-listen.*
%doc %{_mandir}/man1/context-ls.*
%doc %{_mandir}/man1/context-provide.*
# >> files tests
# << files tests

%changelog
* Sat May 12 2012 Paul Wolneykien <manowar@altlinux.ru> 0.5.27-alt1.427.1
- Take own of the directories, make missing directories.

* Tue Apr 17 2012 Paul Wolneykien <manowar@altlinux.ru> 0.5.27-alt1.427
- Adjust the spec for ALT Linux.

* Mon Jan 31 2011 Fathi Boudra <fathi.boudra@nokia.com> - 0.5.27
- Update to 0.5.27 (BMC#13153)
- Drop remove-docs-build.patch
- Split into more packages: doc, python and tests (BMC#6349)
- Fix upstream URL
- Move the files list from the spec file the yaml file
- Fix rpmlint non-executable-script warning
* Thu Jul 15 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> - 0.5.15
- Update to release tag 0.5.15
* Sun Jul 11 2010 Anas Nashif <anas.nashif@intel.com> - 0.5.8
- Fixed build with new compiler/glibc
* Sun Mar 14 2010 Anas Nashif <anas.nashif@intel.com> - 0.5.8
- Use spectacle
- Fixed all rpmlint errors
* Wed Feb 17 2010 Rusty Lynch <rusty.lynch@intel.com> - 0.5.8
- release 0.5.8
  * Mon Nov 23 2009 Rusty Lynch <rusty.lynch> - 0.5
- Initial packaging
