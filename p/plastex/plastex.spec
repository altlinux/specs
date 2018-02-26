Name: plastex
Version: 0.9.2
Release: alt1.1

Summary: Plastex is a Python-based LaTeX document processing framework
Summary(ru_RU.UTF-8): Plastex - средство для обработки документов LaTex, написанное на Python

License: distributable
Group: Publishing
Url: http://plastex.sourceforge.net
BuildArch: noarch

Packager: Anton Chernyshov <ach@altlinux.org>
Source0: %name-%version.tgz
Source1: %name.pdf

BuildPreReq: python-dev

Requires: dvipng
Requires: ghostscript
Requires: texlive-latex-base

# Automatically added by buildreq on Mon Nov 01 2010 (-bi)
BuildRequires: python-devel

%description
plasTeX is a LaTeX document processing framework written entirely in Python. 
It currently comes bundled with an XHTML renderer (including multiple themes), 
as well as a way to simply dump the document to a generic form of XML. Other 
renderers can be added as well and are planned for future releases.

%description -l ru_RU.UTF-8
Plastex - средство для обработки документов LaTex, написанное на Python. 
В настоящее время оно поставляется со средством рендеринга XHTML (включая
множество тем), а также умеет конвертировать документ в обычный XML. 
Другие средства рендеринга будут добавлены в будущие релизы.

%prep
%setup -n %name

%install
%__python setup.py install --root=%buildroot
%__mkdir_p %buildroot/%_defaultdocdir/%name-%version/licenses
%__cp licenses/* %buildroot/%_defaultdocdir/%name-%version/licenses/
%__cp INSTALL  %buildroot/%_defaultdocdir/%name-%version/
%__cp LICENSE  %buildroot/%_defaultdocdir/%name-%version/
%__cp README   %buildroot/%_defaultdocdir/%name-%version/
%__cp TODO     %buildroot/%_defaultdocdir/%name-%version/
%__cp %{SOURCE1} %buildroot/%_defaultdocdir/%name-%version/
%find_lang %name

%files -f %name.lang
%_bindir/*
%python_sitelibdir/*
%doc %_defaultdocdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-2.7

* Mon Nov 1 2010 Anton Chernyshov <ach@altlinux.org> 0.9.2-alt1
- create spec file
- add documentation to package


