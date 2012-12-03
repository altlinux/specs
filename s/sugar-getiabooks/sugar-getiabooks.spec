# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-getiabooks
Version:        11
Release:        alt1_1
Summary:        Internet Archive Books receiver for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Get_Internet_Archive_Books
Source0:        http://download.sugarlabs.org/sources/honey/GetBooks/GetBooks-11.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar
Source44: import.info


%description
This Activity will use the Advanced Search capabilities of the
Internet Archive website to enable browsing the website's catalog,
getting information on the books therein, and downloading these
books to the Journal. Its user interface is similar to the offline
catalog search of Read Etexts, but where that Activity is used for
both getting books and reading them this one will concern itself
only with getting the books, so they may be read with the Read
Activity. 


%prep
%setup -q -n GetBooks-%{version}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{sugaractivitydir}GetBooks.activity/NEWS

#%find_lang org.laptop.GetIABooks.activity
%find_lang org.laptop.sugar.GetBooksActivity

%files -f org.laptop.sugar.GetBooksActivity.lang
%doc NEWS
%{sugaractivitydir}/GetBooks.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 11-alt1_1
- new version; import from fc17 updates

