%define ver 2.3.3
%define reldate 20120624
%define oname objects.inv
Name: python-module-%oname
Version: %ver.%reldate
Release: alt2
Summary: Resource for build documentarion by Sphinx
License: BSD
Group: Development/Python
Url: http://docs.python.org/dev/objects.inv
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source: http://docs.python.org/dev/objects.inv
Source: objects.inv.tar

BuildPreReq: wget rpm-build-python3

%description
This package contains weekly updated Sphinx inventory (version 2,
Project: Python, Version: 3.3) for build documentation by Sphinx.

%package -n python3-module-%oname
Summary: Resource for build documentarion by Sphinx (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This package contains weekly updated Sphinx inventory (version 2,
Project: Python, Version: 3.3) for build documentation by Sphinx.

%prep
%setup

%build

%install
install -d %buildroot%python_sitelibdir/sphinx
install -m644 objects.inv \
	%buildroot%python_sitelibdir/sphinx

install -d %buildroot%python3_sitelibdir/sphinx
install -m644 objects.inv \
	%buildroot%python3_sitelibdir/sphinx

%files
%dir %python_sitelibdir/sphinx
%python_sitelibdir/sphinx/*

%files -n python3-module-%oname
%dir %python3_sitelibdir/sphinx
%python3_sitelibdir/sphinx/*

%changelog
* Sun Jun 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120624-alt2
- repocop cronbuild 20120624. At your service.

* Sat Jun 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120623-alt2
- repocop cronbuild 20120623. At your service.

* Fri Jun 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120622-alt2
- repocop cronbuild 20120622. At your service.

* Sun Jun 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120617-alt2
- repocop cronbuild 20120617. At your service.

* Fri Jun 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120615-alt2
- repocop cronbuild 20120615. At your service.

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120613-alt2
- repocop cronbuild 20120613. At your service.

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120612-alt2
- repocop cronbuild 20120612. At your service.

* Fri Jun 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120608-alt2
- repocop cronbuild 20120608. At your service.

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120606-alt2
- repocop cronbuild 20120606. At your service.

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120605-alt2
- repocop cronbuild 20120605. At your service.

* Sun Jun 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120603-alt2
- repocop cronbuild 20120603. At your service.

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120529-alt2
- repocop cronbuild 20120529. At your service.

* Sun May 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120527-alt2
- repocop cronbuild 20120527. At your service.

* Sat May 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120526-alt2
- repocop cronbuild 20120526. At your service.

* Fri May 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120525-alt2
- repocop cronbuild 20120525. At your service.

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120521-alt2
- repocop cronbuild 20120521. At your service.

* Sat May 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120519-alt2
- repocop cronbuild 20120519. At your service.

* Fri May 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120518-alt2
- repocop cronbuild 20120518. At your service.

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120515-alt2
- repocop cronbuild 20120515. At your service.

* Sun May 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120513-alt2
- repocop cronbuild 20120513. At your service.

* Fri May 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120511-alt2
- repocop cronbuild 20120511. At your service.

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120508-alt2
- repocop cronbuild 20120508. At your service.

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120501-alt2
- repocop cronbuild 20120501. At your service.

* Sun Apr 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120429-alt2
- repocop cronbuild 20120429. At your service.

* Thu Apr 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120426-alt2
- repocop cronbuild 20120426. At your service.

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120425-alt2
- repocop cronbuild 20120425. At your service.

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120424-alt2
- repocop cronbuild 20120424. At your service.

* Thu Apr 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120419-alt2
- repocop cronbuild 20120419. At your service.

* Wed Apr 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120418-alt2
- repocop cronbuild 20120418. At your service.

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120417-alt2
- repocop cronbuild 20120417. At your service.

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3.20120413-alt2
- Fixed for cronbuild

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3.20120413-alt1
- Added module for Python 3

* Sat Apr 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120407-alt1.1
- repocop cronbuild 20120407. At your service.

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120403-alt1.1
- repocop cronbuild 20120403. At your service.

* Sun Apr 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120401-alt1.1
- repocop cronbuild 20120401. At your service.

* Sat Mar 31 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120331-alt1.1
- repocop cronbuild 20120331. At your service.

* Fri Mar 30 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120330-alt1.1
- repocop cronbuild 20120330. At your service.

* Wed Mar 28 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120328-alt1.1
- repocop cronbuild 20120328. At your service.

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120327-alt1.1
- repocop cronbuild 20120327. At your service.

* Thu Mar 22 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120322-alt1.1
- repocop cronbuild 20120322. At your service.

* Wed Mar 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120321-alt1.1
- repocop cronbuild 20120321. At your service.

* Fri Mar 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120316-alt1.1
- repocop cronbuild 20120316. At your service.

* Thu Mar 15 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120315-alt1.1
- repocop cronbuild 20120315. At your service.

* Mon Mar 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120305-alt1.1
- repocop cronbuild 20120305. At your service.

* Sun Mar 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120304-alt1.1
- repocop cronbuild 20120304. At your service.

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120301-alt1.1
- repocop cronbuild 20120301. At your service.

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120229-alt1.1
- repocop cronbuild 20120229. At your service.

* Mon Feb 27 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120227-alt1.1
- repocop cronbuild 20120227. At your service.

* Sat Feb 25 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120225-alt1.1
- repocop cronbuild 20120225. At your service.

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120221-alt1.1
- repocop cronbuild 20120221. At your service.

* Mon Feb 20 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120220-alt1.1
- repocop cronbuild 20120220. At your service.

* Sat Feb 18 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120218-alt1.1
- repocop cronbuild 20120218. At your service.

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120216-alt1.1
- repocop cronbuild 20120216. At your service.

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120209-alt1.1
- repocop cronbuild 20120209. At your service.

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120208-alt1.1
- repocop cronbuild 20120208. At your service.

* Mon Feb 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120206-alt1.1
- repocop cronbuild 20120206. At your service.

* Sun Feb 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120205-alt1.1
- repocop cronbuild 20120205. At your service.

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120131-alt1.1
- repocop cronbuild 20120131. At your service.

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120126-alt1.1
- repocop cronbuild 20120126. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120124-alt1.1
- repocop cronbuild 20120124. At your service.

* Sat Jan 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120121-alt1.1
- repocop cronbuild 20120121. At your service.

* Thu Jan 19 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120119-alt1.1
- repocop cronbuild 20120119. At your service.

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120118-alt1.1
- repocop cronbuild 20120118. At your service.

* Sun Jan 15 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120115-alt1.1
- repocop cronbuild 20120115. At your service.

* Sat Jan 14 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120114-alt1.1
- repocop cronbuild 20120114. At your service.

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120113-alt1.1
- repocop cronbuild 20120113. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120104-alt1.1
- repocop cronbuild 20120104. At your service.

* Sun Jan 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120101-alt1.1
- repocop cronbuild 20120101. At your service.

* Sat Dec 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111224-alt1.1
- repocop cronbuild 20111224. At your service.

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111223-alt1.1
- repocop cronbuild 20111223. At your service.

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111222-alt1.1
- repocop cronbuild 20111222. At your service.

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111221-alt1.1
- repocop cronbuild 20111221. At your service.

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111220-alt1.1
- repocop cronbuild 20111220. At your service.

* Mon Dec 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111219-alt1.1
- repocop cronbuild 20111219. At your service.

* Sat Dec 17 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111217-alt1.1
- repocop cronbuild 20111217. At your service.

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111216-alt1.1
- repocop cronbuild 20111216. At your service.

* Mon Dec 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111212-alt1.1
- repocop cronbuild 20111212. At your service.

* Sun Dec 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111211-alt1.1
- repocop cronbuild 20111211. At your service.

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111210-alt1.1
- repocop cronbuild 20111210. At your service.

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111208-alt1.1
- repocop cronbuild 20111208. At your service.

* Sat Dec 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111203-alt1.1
- repocop cronbuild 20111203. At your service.

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.20111023-alt1.1
- Rebuild with Python-2.7

* Sun Oct 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111023-alt1
- repocop cronbuild 20111023. At your service.

* Thu Oct 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111020-alt1
- repocop cronbuild 20111020. At your service.

* Mon Oct 17 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111017-alt1
- repocop cronbuild 20111017. At your service.

* Fri Oct 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111014-alt1
- repocop cronbuild 20111014. At your service.

* Wed Oct 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111012-alt1
- repocop cronbuild 20111012. At your service.

* Wed Sep 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110928-alt1
- repocop cronbuild 20110928. At your service.

* Mon Sep 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110919-alt1
- repocop cronbuild 20110919. At your service.

* Mon Sep 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110912-alt1
- repocop cronbuild 20110912. At your service.

* Tue Sep 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110906-alt1
- repocop cronbuild 20110906. At your service.

* Sat Sep 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110903-alt1
- repocop cronbuild 20110903. At your service.

* Thu Sep 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110901-alt1
- repocop cronbuild 20110901. At your service.

* Tue Aug 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110823-alt1
- repocop cronbuild 20110823. At your service.

* Mon Aug 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110822-alt1
- repocop cronbuild 20110822. At your service.

* Fri Aug 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110819-alt1
- repocop cronbuild 20110819. At your service.

* Sat Aug 13 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110813-alt1
- repocop cronbuild 20110813. At your service.

* Thu Aug 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110811-alt1
- repocop cronbuild 20110811. At your service.

* Wed Aug 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110810-alt1
- repocop cronbuild 20110810. At your service.

* Mon Aug 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110808-alt1
- repocop cronbuild 20110808. At your service.

* Wed Aug 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110803-alt1
- repocop cronbuild 20110803. At your service.

* Sat Jul 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110730-alt1
- repocop cronbuild 20110730. At your service.

* Fri Jul 29 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110729-alt1
- repocop cronbuild 20110729. At your service.

* Thu Jul 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110721-alt1
- repocop cronbuild 20110721. At your service.

* Mon Jul 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110718-alt1
- repocop cronbuild 20110718. At your service.

* Fri Jul 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110715-alt1
- repocop cronbuild 20110715. At your service.

* Mon Jul 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110711-alt1
- repocop cronbuild 20110711. At your service.

* Sat Jul 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110709-alt1
- repocop cronbuild 20110709. At your service.

* Fri Jul 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110701-alt1
- repocop cronbuild 20110701. At your service.

* Tue Jun 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110628-alt1
- repocop cronbuild 20110628. At your service.

* Mon Jun 27 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110627-alt1
- repocop cronbuild 20110627. At your service.

* Sun Jun 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110626-alt1
- repocop cronbuild 20110626. At your service.

* Sat Jun 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110625-alt1
- repocop cronbuild 20110625. At your service.

* Mon Jun 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110620-alt1
- repocop cronbuild 20110620. At your service.

* Sun Jun 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110619-alt1
- repocop cronbuild 20110619. At your service.

* Sat Jun 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110611-alt1
- repocop cronbuild 20110611. At your service.

* Fri Jun 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110610-alt1
- repocop cronbuild 20110610. At your service.

* Thu Jun 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110609-alt1
- repocop cronbuild 20110609. At your service.

* Wed Jun 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110608-alt1
- repocop cronbuild 20110608. At your service.

* Mon Jun 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110606-alt1
- repocop cronbuild 20110606. At your service.

* Fri Jun 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110603-alt1
- repocop cronbuild 20110603. At your service.

* Thu Jun 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110602-alt1
- repocop cronbuild 20110602. At your service.

* Tue May 31 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110531-alt1
- repocop cronbuild 20110531. At your service.

* Sun May 29 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110529-alt1
- repocop cronbuild 20110529. At your service.

* Wed May 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110525-alt1
- repocop cronbuild 20110525. At your service.

* Tue May 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110524-alt1
- repocop cronbuild 20110524. At your service.

* Mon May 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110523-alt1
- repocop cronbuild 20110523. At your service.

* Sun May 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110515-alt1
- repocop cronbuild 20110515. At your service.

* Mon May 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110509-alt1
- repocop cronbuild 20110509. At your service.

* Sun May 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110508-alt1
- repocop cronbuild 20110508. At your service.

* Fri May 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110506-alt1
- repocop cronbuild 20110506. At your service.

* Mon May 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110502-alt1
- repocop cronbuild 20110502. At your service.

* Sat Apr 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110430-alt1
- repocop cronbuild 20110430. At your service.

* Fri Apr 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110422-alt1
- repocop cronbuild 20110422. At your service.

* Thu Apr 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110421-alt1
- repocop cronbuild 20110421. At your service.

* Wed Apr 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110420-alt1
- repocop cronbuild 20110420. At your service.

* Tue Apr 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110419-alt1
- repocop cronbuild 20110419. At your service.

* Mon Apr 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110418-alt1
- repocop cronbuild 20110418. At your service.

* Fri Apr 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110415-alt1
- repocop cronbuild 20110415. At your service.

* Mon Apr 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110404-alt1
- repocop cronbuild 20110404. At your service.

* Sun Apr 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110403-alt1
- repocop cronbuild 20110403. At your service.

* Thu Mar 31 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110331-alt1
- repocop cronbuild 20110331. At your service.

* Mon Mar 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110328-alt1
- repocop cronbuild 20110328. At your service.

* Thu Mar 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110324-alt1
- repocop cronbuild 20110324. At your service.

* Wed Mar 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110323-alt1
- repocop cronbuild 20110323. At your service.

* Sun Mar 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110320-alt1
- repocop cronbuild 20110320. At your service.

* Fri Mar 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110318-alt1
- repocop cronbuild 20110318. At your service.

* Sat Mar 05 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110305-alt1
- repocop cronbuild 20110305. At your service.

* Tue Mar 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110301-alt1
- repocop cronbuild 20110301. At your service.

* Sat Feb 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110226-alt1
- repocop cronbuild 20110226. At your service.

* Fri Feb 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110225-alt1
- repocop cronbuild 20110225. At your service.

* Wed Feb 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110223-alt1
- repocop cronbuild 20110223. At your service.

* Tue Feb 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110222-alt1
- repocop cronbuild 20110222. At your service.

* Sun Feb 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110220-alt1
- repocop cronbuild 20110220. At your service.

* Sat Feb 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110219-alt1
- repocop cronbuild 20110219. At your service.

* Tue Feb 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110215-alt1
- repocop cronbuild 20110215. At your service.

* Sun Feb 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110206-alt1
- repocop cronbuild 20110206. At your service.

* Fri Feb 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110204-alt1
- repocop cronbuild 20110204. At your service.

* Sun Jan 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110130-alt1
- repocop cronbuild 20110130. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110128-alt1
- repocop cronbuild 20110128. At your service.

* Wed Jan 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110126-alt1
- repocop cronbuild 20110126. At your service.

* Tue Jan 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110125-alt1
- repocop cronbuild 20110125. At your service.

* Sun Jan 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110123-alt1
- repocop cronbuild 20110123. At your service.

* Sun Jan 16 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110116-alt1
- repocop cronbuild 20110116. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110114-alt1
- repocop cronbuild 20110114. At your service.

* Sat Jan 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110108-alt1
- repocop cronbuild 20110108. At your service.

* Thu Jan 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110106-alt1
- repocop cronbuild 20110106. At your service.

* Mon Jan 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110103-alt1
- repocop cronbuild 20110103. At your service.

* Thu Dec 30 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101230-alt1
- repocop cronbuild 20101230. At your service.

* Tue Dec 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101228-alt1
- repocop cronbuild 20101228. At your service.

* Mon Dec 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101227-alt1
- repocop cronbuild 20101227. At your service.

* Sun Dec 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101219-alt1
- repocop cronbuild 20101219. At your service.

* Sat Dec 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101218-alt1
- repocop cronbuild 20101218. At your service.

* Thu Dec 16 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101216-alt1
- repocop cronbuild 20101216. At your service.

* Tue Dec 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101214-alt1
- repocop cronbuild 20101214. At your service.

* Mon Dec 13 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101213-alt1
- repocop cronbuild 20101213. At your service.

* Sun Dec 12 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101212-alt1
- repocop cronbuild 20101212. At your service.

* Tue Dec 07 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101207-alt1
- repocop cronbuild 20101207. At your service.

* Sun Dec 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101205-alt1
- repocop cronbuild 20101205. At your service.

* Sat Dec 04 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101204-alt1
- repocop cronbuild 20101204. At your service.

* Fri Dec 03 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101203-alt1
- repocop cronbuild 20101203. At your service.

* Thu Dec 02 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101202-alt1
- repocop cronbuild 20101202. At your service.

* Wed Dec 01 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101201-alt1
- repocop cronbuild 20101201. At your service.

* Mon Nov 29 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101129-alt1
- repocop cronbuild 20101129. At your service.

* Sun Nov 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101128-alt1
- repocop cronbuild 20101128. At your service.

* Sat Nov 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101127-alt1
- repocop cronbuild 20101127. At your service.

* Tue Nov 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101123-alt1
- repocop cronbuild 20101123. At your service.

* Mon Nov 22 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101122-alt1
- repocop cronbuild 20101122. At your service.

* Sun Nov 21 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101121-alt1
- repocop cronbuild 20101121. At your service.

* Sat Nov 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101120-alt1
- repocop cronbuild 20101120. At your service.

* Fri Nov 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101119-alt1
- repocop cronbuild 20101119. At your service.

* Thu Nov 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101118-alt1
- repocop cronbuild 20101118. At your service.

* Tue Nov 16 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101116-alt1
- repocop cronbuild 20101116. At your service.

* Tue Nov 09 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101109-alt1
- repocop cronbuild 20101109. At your service.

* Sat Nov 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101106-alt1
- repocop cronbuild 20101106. At your service.

* Fri Nov 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101105-alt1
- repocop cronbuild 20101105. At your service.

* Tue Nov 02 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101102-alt1
- repocop cronbuild 20101102. At your service.

* Sat Oct 30 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101030-alt1
- repocop cronbuild 20101030. At your service.

* Thu Oct 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101028-alt1
- repocop cronbuild 20101028. At your service.

* Tue Oct 26 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101026-alt1
- repocop cronbuild 20101026. At your service.

* Mon Oct 25 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101025-alt1
- repocop cronbuild 20101025. At your service.

* Sun Oct 24 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101024-alt1
- repocop cronbuild 20101024. At your service.

* Sat Oct 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101023-alt1
- repocop cronbuild 20101023. At your service.

* Fri Oct 22 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101022-alt1
- repocop cronbuild 20101022. At your service.

* Wed Oct 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101020-alt1
- repocop cronbuild 20101020. At your service.

* Sun Oct 17 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101017-alt1
- repocop cronbuild 20101017. At your service.

* Fri Oct 15 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101015-alt1
- repocop cronbuild 20101015. At your service.

* Thu Oct 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101014-alt1
- repocop cronbuild 20101014. At your service.

* Wed Oct 13 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101013-alt1
- repocop cronbuild 20101013. At your service.

* Mon Oct 11 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101011-alt1
- repocop cronbuild 20101011. At your service.

* Fri Oct 08 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101008-alt1
- repocop cronbuild 20101008. At your service.

* Wed Oct 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101006-alt1
- repocop cronbuild 20101006. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101005-alt1
- repocop cronbuild 20101005. At your service.

* Fri Oct 01 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101001-alt1
- repocop cronbuild 20101001. At your service.

* Tue Sep 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100928-alt1
- repocop cronbuild 20100928. At your service.

* Mon Sep 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100927-alt1
- repocop cronbuild 20100927. At your service.

* Thu Sep 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100923-alt1
- repocop cronbuild 20100923. At your service.

* Tue Sep 21 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100921-alt1
- repocop cronbuild 20100921. At your service.

* Mon Sep 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100920-alt1
- repocop cronbuild 20100920. At your service.

* Sun Sep 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100919-alt1
- repocop cronbuild 20100919. At your service.

* Sat Sep 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100918-alt1
- repocop cronbuild 20100918. At your service.

* Fri Sep 17 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100917-alt1
- repocop cronbuild 20100917. At your service.

* Wed Sep 15 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100915-alt1
- repocop cronbuild 20100915. At your service.

* Tue Sep 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100914-alt1
- repocop cronbuild 20100914. At your service.

* Sat Sep 11 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100911-alt1
- repocop cronbuild 20100911. At your service.

* Fri Sep 10 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100910-alt1
- repocop cronbuild 20100910. At your service.

* Wed Sep 08 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100908-alt1
- repocop cronbuild 20100908. At your service.

* Tue Sep 07 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100907-alt1
- repocop cronbuild 20100907. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100906-alt1
- repocop cronbuild 20100906. At your service.

* Sun Sep 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100905-alt1
- repocop cronbuild 20100905. At your service.

* Sat Sep 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100904-alt1
- online db update 20100904. At your service.

* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100901-alt1
- online db update 20100901. At your service.

* Tue Aug 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100831-alt1
- online db update 20100831. At your service.

* Sat Aug 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100828-alt1
- online db update 20100828. At your service.

* Wed Aug 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100825-alt1
- online db update 20100825. At your service.

* Sun Aug 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100822-alt1
- online db update 20100822. At your service.

* Thu Aug 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100819-alt1
- online db update 20100819. At your service.

* Mon Aug 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100816-alt1
- online db update 20100816. At your service.

* Fri Aug 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100813-alt1
- online db update 20100813. At your service.

* Tue Aug 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100810-alt1
- online db update 20100810. At your service.

* Sat Aug 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100807-alt1
- online db update 20100807. At your service.

* Wed Aug 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100804-alt1
- online db update 20100804. At your service.

* Sun Aug 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100801-alt1
- online db update 20100801. At your service.

* Sat Jul 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100731-alt1
- online db update 20100731. At your service.

* Wed Jul 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100728-alt1
- online db update 20100728. At your service.

* Sun Jul 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100725-alt1
- online db update 20100725. At your service.

* Thu Jul 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100722-alt1
- online db update 20100722. At your service.

* Mon Jul 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100719-alt1
- online db update 20100719. At your service.

* Fri Jul 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100716-alt1
- online db update 20100716. At your service.

* Tue Jul 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100713-alt1
- online db update 20100713. At your service.

* Sat Jul 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100710-alt1
- online db update 20100710. At your service.

* Wed Jul 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100707-alt1
- online db update 20100707. At your service.

* Sun Jul 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100704-alt1
- online db update 20100704. At your service.

* Thu Jul 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100701-alt1
- online db update 20100701. At your service.

* Mon Jun 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100628-alt1
- online db update 20100628. At your service.

* Fri Jun 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100625-alt1
- online db update 20100625. At your service.

* Tue Jun 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100622-alt1
- online db update 20100622. At your service.

* Sat Jun 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100619-alt1
- online db update 20100619. At your service.

* Wed Jun 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100616-alt1
- online db update 20100616. At your service.

* Sun Jun 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100613-alt1
- online db update 20100613. At your service.

* Thu Jun 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100610-alt1
- online db update 20100610. At your service.

* Mon Jun 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100607-alt1
- online db update 20100607. At your service.

* Fri Jun 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100604-alt1
- online db update 20100604. At your service.

* Tue Jun 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100601-alt1
- online db update 20100601. At your service.

* Mon May 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100531-alt1
- online db update 20100531. At your service.

* Fri May 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100528-alt1
- online db update 20100528. At your service.

* Tue May 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100525-alt1
- online db update 20100525. At your service.

* Sat May 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100522-alt1
- online db update 20100522. At your service.

* Wed May 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100519-alt1
- online db update 20100519. At your service.

* Sun May 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100516-alt1
- online db update 20100516. At your service.

* Thu May 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100513-alt1
- online db update 20100513. At your service.

* Mon May 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100510-alt1
- online db update 20100510. At your service.

* Fri May 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100507-alt1
- online db update 20100507. At your service.

* Tue May 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100504-alt1
- online db update 20100504. At your service.

* Sat May 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100501-alt1
- online db update 20100501. At your service.

* Wed Apr 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100428-alt1
- online db update 20100428. At your service.

* Sun Apr 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100425-alt1
- online db update 20100425. At your service.

* Thu Apr 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100422-alt1
- online db update 20100422. At your service.

* Mon Apr 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100419-alt1
- online db update 20100419. At your service.

* Fri Apr 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100416-alt1
- online db update 20100416. At your service.

* Tue Apr 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100413-alt1
- online db update 20100413. At your service.

* Sat Apr 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100410-alt1
- online db update 20100410. At your service.

* Wed Apr 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100407-alt1
- online db update 20100407. At your service.

* Sun Apr 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100404-alt1
- online db update 20100404. At your service.

* Thu Apr 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100401-alt1
- online db update 20100401. At your service.

* Wed Mar 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100331-alt1
- online db update 20100331. At your service.

* Sun Mar 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100328-alt1
- online db update 20100328. At your service.

* Thu Mar 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100325-alt1
- online db update 20100325. At your service.

* Mon Mar 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100322-alt1
- online db update 20100322. At your service.

* Fri Mar 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100319-alt1
- online db update 20100319. At your service.

* Tue Mar 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100316-alt1
- online db update 20100316. At your service.

* Sat Mar 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100313-alt1
- online db update 20100313. At your service.

* Wed Mar 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100310-alt1
- online db update 20100310. At your service.

* Sun Mar 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100307-alt1
- online db update 20100307. At your service.

* Thu Mar 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100304-alt1
- online db update 20100304. At your service.

* Mon Mar 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100301-alt1
- online db update 20100301. At your service.

* Sat Feb 20 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100220-alt2
- online db update 20100220. At your service.

* Mon Feb 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100215-alt2
- online db update 20100215. At your service.

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100209-alt2
- online db update 20100209. At your service.

* Sun Feb 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100207-alt2
- online db update 20100207. At your service.

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100206-alt2
- Repocop Q. A. Robot is ready to be promoted to Maintainer Obvious.

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100206-alt1
- Version 1.2.7.20100206

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100204-alt1
- Version 1.2.7.20100204

* Sun Jan 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100131-alt1
- Avoided remove comment lines from inventory

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100129-alt1
- Initial build for Sisyphus

