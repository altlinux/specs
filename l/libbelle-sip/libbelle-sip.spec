Name: libbelle-sip
Version: 1.6.3
Release: alt4

Summary: Linphone SIP stack
License: GPL
Group: System/Libraries

Url: http://www.belle-sip.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Alexei Takaseev <taf@altlinux.ru>

# Automatically added by buildreq on Thu Mar 02 2017
# optimized out: antlr3-C bcunit gnu-config java-1.8.0-openjdk-headless libstdc++-devel perl pkg-config python-base python3
BuildRequires: antlr3-C-devel java-devel libmbedtls-devel libbctoolbox-devel gcc8-c++ zlib-devel

BuildRequires: /proc rpm-build-java

%description
Belle-sip is an object oriented c written SIP stack used by Linphone.

%package devel
Summary: Development libraries for belle-sip
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and headers required to develop software with belle-sip

%prep
%setup
%patch -p1
%ifarch %e2k
%add_optflags -std=c11
# -Werror => 'unrecognized character escape sequence' gets fatal
# NB: src/grammars/belle_sip_message.g is *not* to be changed
sed -r -i 's,\\(%%[dsu]),\1,g' src/belle_sip_utils.c src/parserutils.h
# as of lcc-1.23.12; looks like author knows of getTokenNames/freeScope warning
sed -i 's,-fms-extensions,-Wno-error=unused-function -Wno-error=unused-variable -Wno-error=ignored-qualifiers,' configure*
%endif

%build
%ifnarch %e2k
%set_gcc_version 8
export CC="gcc-%{_gcc_version}"
export CXX="g++-%{_gcc_version}"
%endif
%autoreconf
%configure \
	--disable-static \
	--with-antlr=%_builddir/%name-%version \
	--enable-strict=no

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install

%makeinstall

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/belle-sip
%_libdir/libbellesip.so
%_libdir/pkgconfig/belle-sip.pc

%changelog
* Thu Oct 24 2019 Alexei Takaseev <taf@altlinux.org> 1.6.3-alt4
- Build with GCC 8

* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 1.6.3-alt3
- E2K: fix ftbfs with lcc 1.23.12
- Build with current compiler version (but without -Werror then)
- Enable parallel build
- Spec cleanup

* Wed Feb 21 2018 Alexei Takaseev <taf@altlinux.org> 1.6.3-alt2
- Add %%set_gcc_version 5 to %%build section

* Sat Jul 22 2017 Alexei Takaseev <taf@altlinux.org> 1.6.3-alt1
- 1.6.3

* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- 1.6.1

* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 1.5.0-alt1
- 1.5.0
- Use system libmbedtls

* Mon Feb 15 2016 Alexei Takaseev <taf@altlinux.org> 1.4.2-alt2
- Add patch for antlr >= 3.4

* Tue Nov 03 2015 Alexei Takaseev <taf@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Jul 30 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt3
- Disable system libmbedtls, use polarssl from linphone.org

* Wed Jun 24 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt2
- Rebuild with new libmbedtls-1.3.11

* Wed May 06 2015 Alexei Takaseev <taf@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Mar 12 2015 Alexei Takaseev <taf@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Sep 19 2014 Alexei Takaseev <taf@altlinux.org> 1.3.3-alt1
- 1.3.3

* Fri Aug 08 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt4
- Rebuild with polarssl-1.3.8

* Tue Apr 22 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt3
- Rebuild with polarssl-1.3.6

* Sat Mar 01 2014 Alexei Takaseev <taf@altlinux.org> 1.3.0-alt2
- Add TLS transport

* Tue Feb 25 2014 Alexei Takaseev <taf@altlinux.ru> 1.3.0-alt1
- Initial build for ALT Sisyphus

* Mon Aug 19 2013 jehan.monnier <jehan.monnier@linphone.org>
- Initial RPM release.
