Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/expect /usr/bin/m4 /usr/bin/makeinfo /usr/bin/runtest liblzma-devel libzstd-devel swig texinfo
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define target avr

Name:           %{target}-gcc
#FIXME:11.2 fails with Werror-format-security https://gcc.gnu.org/bugzilla/show_bug.cgi?id=100431
#revert -Wno-format-security once fix is available
Version:        13.2.0
Release:        alt1_1
Epoch:          1
Summary:        Cross Compiling GNU GCC targeted at %{target}
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            http://gcc.gnu.org/
Source0:        http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
Source2:        README.fedora

Patch0:         avr-gcc-4.5.3-mint8.patch
Patch1:		avr-gcc-config.patch

BuildRequires:  gcc-c++
BuildRequires:  %{target}-binutils >= 1:2.23, zlib-devel gawk libgmp-devel libgmpxx-devel libmpfr-devel libmpc-devel, flex
#for autoreconf:
BuildRequires:  gettext-tools libasprintf-devel automake
#BuildRequires:  autoconf = 2.69
Requires:       %{target}-binutils >= 1:2.23
Provides:       bundled(libiberty)
Source44: import.info

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.


%package c++
Group: Development/Other
Summary:        Cross Compiling GNU GCC targeted at %{target}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native %{_arch}
platform.


%prep
%setup -q -c
[ -d gcc-%{version} ] || mv gcc-4.7-* gcc-%{version}

pushd gcc-%{version}
%patch0  -p2 -b .mint8
#patch -P1 -p2 -b .config

pushd libiberty
#autoconf -f
popd
pushd intl
#autoconf -f
popd

contrib/gcc_update --touch
popd
cp -a %{SOURCE2} .

# Extract %%__os_install_post into os_install_post~
cat << \EOF > os_install_post~
%__os_install_post
EOF

# Generate customized brp-*scripts
cat os_install_post~ | while read a x y; do
case $a in
# Prevent brp-strip* from trying to handle foreign binaries
*/brp-strip*)
  b=$(basename $a)
  sed -e 's,find "*$RPM_BUILD_ROOT"*,find "$RPM_BUILD_ROOT%_bindir" "$RPM_BUILD_ROOT%_libexecdir",' $a > $b
  chmod a+x $b
  ;;
esac
done

sed -e 's,^[ ]*/usr/lib/rpm.*/brp-strip,./brp-strip,' \
< os_install_post~ > os_install_post 


%build
pushd gcc-%{version}
acv=$(autoreconf --version | head -n1)
acv=${acv##* }
sed -i "/_GCC_AUTOCONF_VERSION/s/2.64/$acv/" config/override.m4
#autoreconf -fiv
pushd intl
#autoreconf -ivf
popd
popd
mkdir -p gcc-%{target}
pushd gcc-%{target}
FILTERED_RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}" | sed 's/Werror=format-security/Wno-format-security/g')
export CFLAGS=$FILTERED_RPM_OPT_FLAGS
export CXXFLAGS=$FILTERED_RPM_OPT_FLAGS
CC="gcc ${FILTERED_RPM_OPT_FLAGS} -fno-stack-protector" \
../gcc-%{version}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --infodir=%{_infodir} --target=%{target} --enable-languages=c,c++ \
  --disable-nls --disable-libssp --with-system-zlib \
  --enable-version-specific-runtime-libs \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/"

make
popd


%install
pushd gcc-%{target}
make install DESTDIR=$RPM_BUILD_ROOT
popd
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a ||:
rm    $RPM_BUILD_ROOT%{_libdir}/libcc1* ||:
# and these aren't usefull for embedded targets
rm -r $RPM_BUILD_ROOT/usr/lib/gcc/%{target}/%{version}/install-tools ||:
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{version}/install-tools ||:

%define __os_install_post . ./os_install_post



%files
%doc --no-dereference gcc-%{version}/COPYING gcc-%{version}/COPYING.LIB
%doc gcc-%{version}/README README.fedora
%{_bindir}/%{target}-*
%dir /usr/lib/gcc
%dir /usr/lib/gcc/%{target}
/usr/lib/gcc/%{target}/%{version}
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{target}
%{_libexecdir}/gcc/%{target}/%{version}
%{_mandir}/man1/%{target}-*.1*
%exclude %{_bindir}/%{target}-?++
%exclude %{_libexecdir}/gcc/%{target}/%{version}/cc1plus
%exclude %{_mandir}/man1/%{target}-g++.1*

%files c++
%{_bindir}/%{target}-?++
%{_libexecdir}/gcc/%{target}/%{version}/cc1plus
%{_mandir}/man1/%{target}-g++.1*


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1:13.2.0-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 1:10.2.0-alt1_1
- update to new release by fcimport

* Sat Oct 10 2020 Igor Vlasenko <viy@altlinux.ru> 1:9.2.0-alt1_6
- rebuild on armh

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 1:9.2.0-alt1_1
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 1:7.4.0-alt1_5
- update to new release by fcimport

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 1:7.2.0-alt1_1
- fixed build

* Fri Feb 03 2017 Grigory Milev <week@altlinux.ru> 4.9.2-alt4
- Updated version from Atmel

* Mon Jun 20 2016 Grigory Milev <week@altlinux.ru> 4.9.2-alt3
- Buildreq cleanup

* Tue May 17 2016 Grigory Milev <week@altlinux.ru> 4.9.2-alt2
- Remove avr-libc from build requires, need for initial ARM build

* Sat Jan 09 2016 Grigory Milev <week@altlinux.ru> 4.9.2-alt1
- New version from Atmel (Toolchain 3.5.0)

* Thu Mar 13 2014 Grigory Milev <week@altlinux.ru> 4.8.1-alt1
- New version released

* Mon Oct 14 2013 Grigory Milev <week@altlinux.ru> 4.7.2-alt3
- Updated version with Atmel patches

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 4.7.2-alt2
- rebuild with new binutils + new avr cpu's

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 4.7.2-alt1
- new version

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt3.1
- Rebuilt with gmp 5.0.5

* Thu Mar 17 2011 Grigory Milev <week@altlinux.ru> 4.5.1-alt3
- added patch for fix problem with USART2 and USART3 on atmega2560

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 4.5.1-alt2
- rebuild with new binutils
- fixed configure scripts

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 4.5.1-alt1
- new version released
- gcc moved to /usr/lib/gcc/avr and /usr/lib/libexec/gcc/avr

* Wed Dec 02 2009 Grigory Milev <week@altlinux.ru> 4.2.2-alt2
- fix build requires

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 4.2.2-alt1
- New version released

* Wed Sep 21 2005 Grigory Milev <week@altlinux.ru> 3.4.4-alt1
- New version released

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 3.3.1-alt1
- 3.3.1 released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 3.3-alt1.20030512
- new cvs snapshot released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 3.3-alt1.20030414
- new cvs snapshot released

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 3.2.75-alt2
- new version (snapshot 20030203)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 3.2.75-alt1.20021028
- new version (snapshot)

* Thu Oct 24 2002 Grigory Milev <week@altlinux.ru> 3.0.4-alt1
- Initial build for ALT Linux

* Tue Mar 17 2002 Theodore A. Roth <troth@verinet.com>
- Initial spec file.

