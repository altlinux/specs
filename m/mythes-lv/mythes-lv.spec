# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-lv
Summary: Latvian mythes dictionaries
Version: 0.9.4
Release: alt1_11
Source: http://dict.dv.lv/download/lv_LV-%{version}.oxt
Group: Text tools
URL: http://dict.dv.lv/
License: LGPLv2+
BuildArch: noarch
Requires: libmythes
Requires: locales-lv
Source44: import.info

%description
Latvian thesaurus.

%prep
%setup -q -c

%build
for i in README_lv_LV.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-4 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
chmod -x *.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lv_LV_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc package-description.txt license.txt
%{_datadir}/mythes/*


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_11
- new version

