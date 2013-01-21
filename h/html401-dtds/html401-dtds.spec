Group: Other
# Note to self: like is with the HTML 2.0 and 3.2 DTDs, HTML 4.0 and 4.01
# have the same public id to their ENTITIES files.  They are not exactly the
# same in 4.0 and 4.01, but the changes are in comments only, so no need
# use a hardcoded system id.  Well, until something installs another, and
# incompatible set of entities using the same public id anyway...

%define date    19991224

Name:           html401-dtds
Version:        4.01
Release:        alt1_19991224.12.2
Summary:        HTML 4.01 document type definitions

# W3C Software License for DTDs etc:
# http://www.w3.org/Consortium/Legal/IPR-FAQ-20000620#DTD
License:        W3C
URL:            http://www.w3.org/TR/1999/REC-html401-%{date}/
# Source0 generated with Source99, see comments in the script
Source0:        %{name}-%{date}.tar.bz2
Source99:       %{name}-prepare-tarball.sh
Patch0:         %{name}-catalog.patch

BuildArch:      noarch
Requires:       xml-common sgml-common
Requires(post): /usr/bin/install-catalog
Requires(preun): /usr/bin/install-catalog
Source44: import.info

%description
This package provides the three HTML 4.01 DTDs (strict, frameset, and
transitional).  The DTDs are required for processing HTML 4.01
document instances using SGML tools such as OpenSP, OpenJade, or
SGMLSpm.


%prep
%setup -q -n %{name}
%patch0 -p1


%build


%install

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/sgml/html/4.01
install -pm 644 *.dtd *.cat *.ent *.decl \
    $RPM_BUILD_ROOT%{_datadir}/sgml/html/4.01

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sgml
cd $RPM_BUILD_ROOT%{_sysconfdir}/sgml
touch %{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{name}.soc
cd -


%post
/usr/bin/install-catalog --add \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null

%preun
/usr/bin/install-catalog --remove \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null || :


%files
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_datadir}/sgml/html/


%changelog
* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1_19991224.12.2
- initial fc import

