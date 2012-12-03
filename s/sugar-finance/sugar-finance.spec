# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-finance
Version:        8
Release:        alt1_1
Summary:        Financial planning for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Finance
Source0:        http://download.sugarlabs.org/sources/honey/Finance/Finance-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires:       sugar
Source44: import.info


%description
Finance is a simple financial planning activity. It can be integrated 
into classroom assignments, or else used to track finances for a school
club. It might also be useful for students who wish to help their parents
with home finances.

The register view allows students to enter income and expenses, assign
categories, and review past transactions. The chart view shows students
a visual breakdown of their expenses by category. The budget view allows
users to assign a monthly budget to each category, and to see how each
month's expenses compare to the budget.


%prep
%setup -q -n Finance-%{version}
chmod -x {icons/help.svg,finance.py}


%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.community.Finance


%files -f org.laptop.community.Finance.lang
%doc COPYING NEWS TODO
%{sugaractivitydir}/Finance.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_1
- new version; import from fc17 updates

