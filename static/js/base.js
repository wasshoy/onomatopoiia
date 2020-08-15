'use strict';
{
  // ヘッダーのユーザー名をクリックするとメニューが出現
  const userMenu = document.getElementById('user-menu');
  const userTab = document.getElementById('user-tab');
  userTab.addEventListener('click', () => {
    userMenu.classList.toggle('hidden');
  });

  // Message to Developers.
  const styles1 =
    ' \
  @import url("https://fonts.googleapis.com/css2?family=Lemon&display=swap"); \
  background: #f7d94c; \
  color:#fefefe; \
  display: block; \
  font-family: serif;\
  font-size:32px; \
  font-weight: bold; \
  padding: 12px 24px; \
  text-shadow: 1px 1px 0 #0ff, -1px -1px 0 #f0f ;\
  ';
  console.log('%c_onomatopoiia_', styles1);
  const style2 = 'color:#f7d94c;';
  console.log(
    '%cメメタア グワラゴワガキーン ざわ... ざわ... クン パパウ パウパウ',
    style2
  );
  console.log(
    '%c かがくの',
    'font-weight: bold; font-size: 50px;color: red; padding-right: 24px; text-shadow: 3px 3px 0 rgb(217,31,38) , 6px 6px 0 rgb(226,91,14) , 9px 9px 0 rgb(245,221,8) , 12px 12px 0 rgb(5,148,68) , 15px 15px 0 rgb(2,135,206) , 18px 18px 0 rgb(4,77,145) , 21px 21px 0 rgb(42,21,113)'
  );
  console.log(
    '%c ちからって',
    'font-weight: bold; font-size: 50px;color: red; padding-right: 24px; text-shadow: 3px 3px 0 rgb(217,31,38) , 6px 6px 0 rgb(226,91,14) , 9px 9px 0 rgb(245,221,8) , 12px 12px 0 rgb(5,148,68) , 15px 15px 0 rgb(2,135,206) , 18px 18px 0 rgb(4,77,145) , 21px 21px 0 rgb(42,21,113)'
  );
  console.log(
    '%c すげー！',
    'font-weight: bold; font-size: 50px;color: red; padding-right: 24px; text-shadow: 3px 3px 0 rgb(217,31,38) , 6px 6px 0 rgb(226,91,14) , 9px 9px 0 rgb(245,221,8) , 12px 12px 0 rgb(5,148,68) , 15px 15px 0 rgb(2,135,206) , 18px 18px 0 rgb(4,77,145) , 21px 21px 0 rgb(42,21,113)'
  );
}
