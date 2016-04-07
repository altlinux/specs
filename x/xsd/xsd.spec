# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           xsd
Version:        3.3.0
Release:        alt2_16.qa1
Summary:        W3C XML schema to C++ data binding compiler

Group:          Development/Tools
# Exceptions permit otherwise GPLv2 incompatible combination with ASL 2.0
License:        GPLv2 with exceptions and ASL 2.0  
URL:            http://www.codesynthesis.com/products/xsd/
Source0:        http://www.codesynthesis.com/download/xsd/3.3/xsd-%{version}-2+dep.tar.bz2
# Sent suggestion to upstream via e-mail 20090707
Patch0:         xsd-3.3.0-xsdcxx-rename.patch

BuildRequires:  m4 boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel xerces-c-devel
Source44: import.info
# Requires:  ace-devel - only needed for applications using
#                        Adaptive Communication Environment (ACE) streams,
#                        enable when Fedora gets ACE packages.
#                        See http://www.cs.wustl.edu/~schmidt/ACE.html and
#                        https://bugzilla.redhat.com/show_bug.cgi?id=450164

%description
CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to
C++ data binding compiler. Provided with an XML instance specification
(XML Schema), it generates C++ classes that represent the given
vocabulary as well as parsing and serialization code.
You can then access the data stored in XML using types and functions
that semantically correspond to your application domain rather than
dealing with intricacies of reading and writing XML.


%package        doc
Group:          Documentation
Summary:        API documentation files for %{name}

%description    doc
This package contains API documentation for %{name}.


%prep
%setup -q -n xsd-%{version}-2+dep
pushd xsd
%patch0 -p1 -b .xsdcxx-rename
popd


%build

# Default GCC on EL-5 will fail on this code with internal
# compiler error when debugging symbol generation is requested with -g
# Reducing debug level to 1 will "fix" this problem. A better way would
# be to use gcc-44, but old versions of boost headers do not compile 
# with it (https://svn.boost.org/trac/boost/ticket/2069).
# Also boost-1.33.1 on those systems does not have boost_system library
# thus we need to disable explicit linking against it.

%if 0%{?el5}
make verbose=1 CXXFLAGS="$RPM_OPT_FLAGS -g1" BOOST_LINK_SYSTEM=n
%else
make verbose=1 CXXFLAGS="$RPM_OPT_FLAGS"
%endif


%install
rm -rf apidocdir

%if 0%{?el5}
make install_prefix="$RPM_BUILD_ROOT%{_prefix}" BOOST_LINK_SYSTEM=n install
%else
make install_prefix="$RPM_BUILD_ROOT%{_prefix}" install
%endif

# Split API documentation to -doc subpackage.
mkdir apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/*.{xhtml,css} apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/cxx/ apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/ docdir/

# Convert to utf-8.
for file in docdir/NEWS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

# Rename binary to xsdcxx to avoid conflicting with mono-web package.
# Sent suggestion to upstream via e-mail 20090707
# they will consider renaming in 4.0.0
mv $RPM_BUILD_ROOT%{_bindir}/xsd $RPM_BUILD_ROOT%{_bindir}/xsdcxx
mv $RPM_BUILD_ROOT%{_mandir}/man1/xsd.1 $RPM_BUILD_ROOT%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxsd

# Remove Microsoft Visual C++ compiler helper files.
rm -rf $RPM_BUILD_ROOT%{_includedir}/xsd/cxx/compilers

# Remove redundant PostScript files that rpmlint grunts about not being UTF8
# See: https://bugzilla.redhat.com/show_bug.cgi?id=502024#c27
# for Boris Kolpackov's explanation about those
find apidocdir -name "*.ps" | xargs rm -f
# Remove other unwanted crap
find apidocdir -name "*.doxygen" \
            -o -name "makefile" \
            -o -name "*.html2ps" | xargs rm -f

%files
%doc docdir/*
%{_bindir}/xsdcxx
%{_includedir}/xsd/
%{_mandir}/man1/xsdcxx.1*

%files doc
%doc apidocdir/*


%changelog
* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.3.0-alt2_16.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Mon Mar 09 2015 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt2_16
- moved to Sisyphus by request of mike@

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_16
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_15
- initial fc import

