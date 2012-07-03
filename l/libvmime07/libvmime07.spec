# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime07
Version:	0.7.1
Release:	alt2_7
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.zarafa.com/wiki/index.php/Libvmime_patches
Source0:	http://developer.zarafa.com/download/libvmime-%{version}.tar.bz2
Patch0:		libvmime07-0.7.1-package.patch
Patch1:		libvmime07-0.7.1-charset-catch.patch
Patch2:		libvmime07-0.7.1-missing-boundary.patch
Patch3:		libvmime07-0.7.1-allow-no-recips-and-senders.patch
Patch4:		libvmime07-0.7.1-bmoted-printable.patch
Patch5:		libvmime07-0.7.1-strip-header-endspaces-and-header-end.patch
Patch6:		libvmime07-0.7.1-attachfnamelen.patch
Patch7:		libvmime07-0.7.1-remove-bcc.patch
Patch8:		libvmime07-0.7.1-mdn-disposition.patch
Patch9:		libvmime07-0.7.1-mdn-final-recipient.patch
Patch10:	libvmime07-0.7.1-broken-locale-error.patch
Patch11:	libvmime07-0.7.1-qp-starts-on-second-line.patch
Patch12:	libvmime07-0.7.1-quoted-printable-specials.patch
Patch13:	libvmime07-0.7.1-header-value-on-next-line.patch
Patch14:	libvmime07-0.7.1-oe-compatibility.patch
Patch15:	libvmime07-0.7.1-unicode-1-1-utf-7-charset.patch
Patch16:	libvmime07-0.7.1-out-of-bounds-copy.patch
Patch17:	libvmime07-0.7.1-default-transfer-encoding.patch
Patch18:	libvmime07-0.7.1-contentid-without-at.patch
Patch19:	libvmime07-0.7.1-socket-backport-and-timeout-fix.patch
Patch20:	libvmime07-0.7.1-double-empty-boundary.patch
Patch21:	libvmime07-0.7.1-quoted-printable-encode-questionmark.patch
Patch22:	libvmime07-0.7.1-charset-output-buffer-full.patch
Patch23:	libvmime07-0.7.1-gcc-4.3-support.patch
Patch24:	libvmime07-0.7.1-timezone-name.patch
Patch25:	libvmime07-0.7.1-socket-tcp-nodelay.patch
Patch26:	libvmime07-0.7.1-threading-remove-static_non-abi-change.patch
Patch27:	libvmime07-0.7.1-gcc-4.4-support.patch
Patch28:	libvmime07-0.7.1-plain-bodycopy.patch
Patch29:	libvmime07-0.7.1-sigset-signal.patch
Patch30:	libvmime07-0.7.1-address-parse-encoded.patch
Patch31:	libvmime07-0.7.1-fullname-without-email-address.patch
Patch32:	libvmime07-0.7.1-strip-spaces-parameterized-headers.patch
Patch33:	libvmime07-0.7.1-allow-alternate-encodings.patch
BuildRequires:	sendmail libtool autoconf automake
Source44: import.info

%description
VMime is a powerful C++ class library for parsing, generating or
editing Internet RFC-[2]822 and MIME messages. VMime is designed
to provide a fast and an easy way to manipulate Internet mail
messages.

It also includes support for using messaging protocols (POP3, IMAP,
SMTP and maildir) with a lot of features supported: listing folders,
downloading and adding messages to folders, extracting parts from
message, getting and setting message flags and a lot more.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%package devel
Summary:	Development files for the libvmime library
Group:		Development/C
Requires:	libvmime07 = %{version}-%{release}

%description devel
The libvmime package includes header files and libraries necessary
for developing programs which use the libvmime C++ class library.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%prep
%setup -q -n libvmime-%{version}
%patch0 -p1 -b .package
%patch1 -p1 -b .charset-catch
%patch2 -p1 -b .missing-boundary
%patch3 -p1 -b .allow-no-recips-and-senders
%patch4 -p1 -b .bmoted-printable
%patch5 -p1 -b .strip-header-endspaces-and-header-end
%patch6 -p1 -b .attachfnamelen
%patch7 -p1 -b .remove-bcc
%patch8 -p1 -b .mdn-disposition
%patch9 -p1 -b .mdn-final-recipient
%patch10 -p1 -b .broken-locale-error
%patch11 -p1 -b .qp-starts-on-second-line
%patch12 -p1 -b .quoted-printable-specials
%patch13 -p1 -b .header-value-on-next-line
%patch14 -p1 -b .oe-compatibility
%patch15 -p1 -b .unicode-1-1-utf-7-charset
%patch16 -p1 -b .out-of-bounds-copy
%patch17 -p1 -b .default-transfer-encoding
%patch18 -p1 -b .contentid-without-at
%patch19 -p1 -b .socket-backport-and-timeout-fix
%patch20 -p1 -b .double-empty-boundary
%patch21 -p1 -b .quoted-printable-encode-questionmark
%patch22 -p1 -b .charset-output-buffer-full
%patch23 -p1 -b .gcc-4.3-support
%patch24 -p1 -b .timezone-name
%patch25 -p1 -b .socket-tcp-nodelay
%patch26 -p1 -b .threading-remove-static_non-abi-change
%patch27 -p1 -b .gcc-4.4-support
%patch28 -p1 -b .plain-bodycopy
%patch29 -p1 -b .sigset-signal
%patch30 -p1 -b .address-parse-encoded
%patch31 -p1 -b .fullname-without-email-address
%patch32 -p1 -b .strip-spaces-parameterized-headers
%patch33 -p1 -b .allow-alternate-encodings

# Needed to apply branding patch
libtoolize --force
autoreconf --force --install

%build
export EXTRA_CFLAGS="$RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Complete the libvmime07 renaming at some places
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}/
mv -f $RPM_BUILD_ROOT%{_includedir}/{vmime,%{name}}/
mv -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/vmime{,07}.pc 

# Remove the static library and libtool .la file
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.{a,la}

# Remove the documentation dir, as %doc will pick it up
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/vmime07.pc

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_7
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_6
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_5
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_5
- initial import by fcimport

