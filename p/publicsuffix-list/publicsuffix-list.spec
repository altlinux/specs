Group: Networking/Other
%global revdate 20151208

Name:           publicsuffix-list
Version:        %{revdate}
Release:        alt1_1
Summary:        Cross-vendor public domain suffix database

License:        MPLv2.0
URL:            https://publicsuffix.org/
Source0:        https://publicsuffix.org/list/public_suffix_list.dat
Source1:        https://www.mozilla.org/MPL/2.0/index.txt
Source2:        https://github.com/publicsuffix/list/raw/master/tests/test_psl.txt

BuildArch:      noarch
Source44: import.info


%description
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.


%prep
%setup -c -T
cp -av %{SOURCE1} COPYING


%build


%install
install -m 644 -p -D %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dat
install -m 644 -p -D %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/test_psl.txt
ln -s public_suffix_list.dat $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/effective_tld_names.dat


%files
%doc COPYING
%{_datadir}/publicsuffix


%changelog
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 20151208-alt1_1
- to Sisyphus

