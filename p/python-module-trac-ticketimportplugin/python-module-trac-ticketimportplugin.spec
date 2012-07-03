%define tarname ticketimportplugin
Name: python-module-trac-ticketimportplugin
%define r_minor r9770
Version: 0.8
Release: alt1.%r_minor.1

Summary: Import CSV and Excel files

Group: Development/Python
# FIXME: unknown?
License: BSD
Url: http://trac-hacks.org/wiki/TicketImportPlugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
This plugin lets you import into Trac a series of tickets from a CSV file or 
(if the xlrd library is installed) from an Excel file. You can also use it to 
modify tickets in batch, by saving a report as CSV, editing the CSV file, and 
re-importing the tickets. This plugin is very useful when starting a new project:
you can import a list of requirements that may have come from meeting notes,
list of features, other ticketing systems... It's also great to review the
tickets off-line, or to do massive changes to tickets. Based on the ticket id 
(or, if no id exists, on the summary) in the imported file, tickets are either
created or updated.

%prep
%setup -q -n %tarname/0.11

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

chmod -R a+r %buildroot%python_sitelibdir/talm_importer

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.r9770.1
- Rebuild with Python-2.7

* Mon Jan 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8-alt1.r9770
- Build for ALT
