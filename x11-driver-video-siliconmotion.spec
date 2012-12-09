Name: x11-driver-video-siliconmotion
Version: 1.7.7
Release: 2
Summary: X.org driver for Silicon Motion Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-siliconmotion-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-siliconmotion is
the X.org driver for Silicon Motion Cards.

%prep
%setup -qn xf86-video-siliconmotion-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.7-1
+ Revision: 810700
- version update 1.7.7
- version update 1.7.7

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.7.6-2
+ Revision: 787269
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.6-1
+ Revision: 786717
- version update 1.7.6

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.7.5-5
+ Revision: 748456
- rebuild cleaned up spec

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.7.5-3
+ Revision: 683586
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.5-2
+ Revision: 671170
- mass rebuild

* Mon Feb 28 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.7.5-1
+ Revision: 640989
- New version: 1.7.5

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.7.4-3mdv2011.0
+ Revision: 595735
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.7.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Wed Apr 28 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.7.4-1mdv2010.1
+ Revision: 540405
- New version: 1.7.4
- Use %%configure2_5x
- Don't need to autoreconf

* Wed Aug 05 2009 Thierry Vignaud <tv@mandriva.org> 1.7.3-1mdv2010.0
+ Revision: 410244
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.7.2-1mdv2010.0
+ Revision: 391931
- update to new version 1.7.2

* Thu Apr 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.7.1-1mdv2010.0
+ Revision: 369181
- New version 1.7.1

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.7.0-1mdv2009.1
+ Revision: 321389
- New version 1.7.0
- Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.6.0-3mdv2009.1
+ Revision: 308242
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.6.0-2mdv2009.0
+ Revision: 265930
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Thierry Vignaud <tv@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 212432
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.5.1-4mdv2009.0
+ Revision: 194158
- Update to version 1.6.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.5.1-4mdv2008.1
+ Revision: 166109
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.5.1-3mdv2008.1
+ Revision: 156619
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.5.1-2mdv2008.1
+ Revision: 154795
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to properly generate the tarball from tag
  xf86-video-siliconmotion-1.5.1, and also include some patches considered
  ok, but without hardware to test, and the previously created mandriva
  branch was not moved.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.5.1-1mdv2008.1
+ Revision: 99032
- new upstream version: 1.5.1
- minor spec cleanup

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdv2008.0
+ Revision: 75786
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

