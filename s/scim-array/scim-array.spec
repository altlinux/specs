Name: scim-array
Version: 1.0.1
Release: alt1
Summary: SCIM Array 30 Input Method Engine

Group: System/Libraries
License: GPLv2+
Url: http://scimarray.openfoundry.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://of.openfoundry.org/download_path/scimarray/%version/%name-%version.tar.gz
#Patch0:        %name.patch

BuildRequires: scim-devel gettext gettext-tools gcc-c++
Requires: scim

%description
SCIM Array 30 Input Method Engine provides with all the functions of Array 30,
including 1st and 2nd level short codes, special codes, and symbol input.


%prep
%setup -q
#%patch0 -p0 -b .bak

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%_libdir/scim-1.0/1.4.0/IMEngine/array.la
rm -f $RPM_BUILD_ROOT%_libdir/scim-1.0/1.4.0/SetupUI/*.la

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/scim-1.0/1.4.0/IMEngine/array.so
%_libdir/scim-1.0/1.4.0/SetupUI/array-imengine-setup.so
%_datadir/scim/Array
%_datadir/scim/icons/scim-array.png

%changelog
* Sun Dec 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt1
- Build for ALT Linux

* Wed Nov 26 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.0.1-0
- Upstream update to 1.0.1

* Tue May 20 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.0.0-0
- Upstream update to 1.0.0

* Fri Feb 15 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.0.4
- Update to 0.0.4

* Thu Feb 14 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.0.3-2
- Build with GCC4.3
* Tue Feb 12 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.0.3-0
- Update to 0.0.3
* Wed Oct 31 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.2-1
- Correct URL
* Wed Aug 29 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.2-0
- Update to 0.0.2
* Fri Aug 17 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.1-4
- Remove tags in the changelog section
* Fri Aug 17 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.1-3
- Remove following files in file section
  scim/Array/array-shortcode.cin
  scim/Array/array-special.cin
  scim/Array/array30.cin
* Fri Aug 17 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.1-2
- Add scim/Array in file section.
* Fri Aug 17 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.1-1
- Update spec file according to Bugzilla (#253805).
* Fri Aug 17 2007 Ding-Yi Chen <dchen at redhat dot com> - 0.0.1-0
- initial packaging

