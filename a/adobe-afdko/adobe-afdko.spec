Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global archivename afdko

Name:		adobe-afdko
Version:	3.6.1
Release:	alt1_3
Summary:	Adobe Font Development Kit for OpenType
License:	ASL 2.0
URL:		https://github.com/adobe-type-tools/afdko
Source0:	https://github.com/adobe-type-tools/%{archivename}/releases/download/%{version}/%{archivename}-%{version}.tar.gz
BuildRequires:	gcc
Source44: import.info

%description
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.

%prep
%setup -q -n %{archivename}-%{version}


%build

pushd c
sh buildalllinux.sh release
popd

%install
install -m 0755 -d %{buildroot}/%{_bindir}
pushd c/build_all
find ./ -type f -executable -exec install -p -m 0755 "{}" \
	%{buildroot}/%{_bindir} ";"

%files
%doc --no-dereference LICENSE.md
%doc docs/ README.md NEWS.md
%{_bindir}/*

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 3.6.1-alt1_3
- update

